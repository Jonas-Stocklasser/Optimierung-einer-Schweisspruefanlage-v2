#!/usr/bin/python3
# Date: 27.07.24
# Author: Stocklasser
# Diplomarbeit, Optimierung einer Schweisspruefanlage
# json functions

import json     # json file handling library
import pandas as pd     # a file reading library


# method to write something to a json file
def json_writer(json_name, variable, value, json_path):
    data = pd.read_json(f"{json_path}{json_name}.json", encoding="utf-8")  # get the dataframe from the file
    index = data.index[data['var'] == variable].tolist()    # find the correct index

    if index:
        data.at[index[0], 'val'] = value    # if the index exists change the value entry
    else:
        new_row = pd.DataFrame([{'var': variable, 'val': value}])   # add a new entry/ index to the dataframe
        data = pd.concat([data, new_row], ignore_index=True)
        print("NEW ROW ADDED")

    with open(f"{json_path}{json_name}.json", "w", encoding="utf-8") as file:
        data.to_json(file, orient="records", indent=2, force_ascii=False)   # write the changed dataframe to the file


# method to read something out of a json file
def json_reader(json_name, variable, json_path):
    with open(f"{json_path}{json_name}.json", encoding="utf-8") as file:
        data = pd.read_json(file)
    if variable in data['var'].values:
        read_value = data.loc[data['var'] == variable, "val"].values[0]
        return read_value
    else:
        print("ERROR WHILE TRYING TO READ")
        print(f"json_name : {json_name}")
        print(f"json_path : {json_path}")
        print(f"variable : {variable}")


# method to create a new json file
def json_creator(json_name, json_path, first_var, first_val):
    data = [    # define the dataframe
        {
            'var': first_var,
            'val': first_val,
        }
    ]
    with open(f"{json_path}{json_name}.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
