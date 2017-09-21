#!/usr/bin/python
# Filename: word_pickup_json

import json
import pandas as pd

# Reading data back
with open('synsets.json', 'r') as f:   # open file
    data = json.load(f) # load .json as python object
    # data = [json.loads(line) for line in f]

# Read word list
with open('word_list.txt', 'r') as word_list:
    list = word_list.readlines()

# pickup sentense with keywords
record = []
for line in list:
    line = line.rstrip()
    df = pd.DataFrame(data, columns=['synset_name', 'synset_definition']).astype(str)
    print line,
    # print type(line)
    # df = df[df['synset_definition'].str.contains(line+"$", case=True)]  # search the independent word, if just search the part include word: delete +"S"
    df = df[df['synset_name'].str.contains(line, case=True) |
            df['synset_definition'].str.contains(line+"$", case=True)]  # search in both rows
    df = df.drop_duplicates()  #delete repeated data
    df = df.sort_index()  # sort data as ascending
    df = df.reset_index()  # sort out new oder of columns
    del df['index']
    record.append(df)
    print df
    df.to_csv(line + ".txt", index=False)  # save as .txt

    # df.to_json(line + ".json")  # save as .json
