#!/usr/bin/python
# Filename: word_pickup_json

import json
import pandas as pd

word_list = open('word_list.txt')
# Reading data back
with open('synsets.json', 'r') as f:   # open file
    data = json.load(f) # load .json as python object
    # data = [json.loads(line) for line in f]
df = pd.DataFrame(data, columns=['synset_name', 'synset_definition']).astype(str)

result = list()
for line in word_list:
    print line
    result.append(line)
    df = df[df['synset_definition'].str.contains("line$")]
    df = df.drop_duplicates()  #delete repeated data
    df = df.sort_index()  # sort data as ascending
    df = df.reset_index()  # sort out new oder of columns
    del df['index']
    print df
    df.to_csv(line+".txt", index=False)  # save as .txt
    # df.to_json(line+".json")  # save as .json
