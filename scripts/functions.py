import os
import numpy as np
import pandas as pd

def get_current_dir():
    directory = __file__
    i = len(directory) - 1
    while directory[i] != "\\":
        directory = directory[:-1]
        i -= 1
    return directory[:-9]

def get_file_ext(file_name):
    i = 0
    while file_name[i] != ".":
        i += 1
    extension = file_name[i:]
    return extension

def get_csv_files(file_list):
    csv_list = []
    for i in range(len(file_list)):
        file_name = file_list[i]
        if get_file_ext(file_name) == ".csv":
            csv_list.append(file_name)
    return csv_list

def index_to_reference(row, col):
    col_letter = ''
    while col >= 0:
        col_letter = chr(col % 26 + ord('A')) + col_letter
        col = col // 26 - 1
    return f"{col_letter}{row + 2}"

def find_positions(dataframe, search_str):
    positions = []
    search_str_lower = search_str.lower()
    for column_name in dataframe.columns:
        column_data = dataframe[column_name].astype(str).str.lower()
        indices = np.where(column_data.str.contains(search_str_lower, na=False))[0]
        col_index = dataframe.columns.get_loc(column_name)
        for index in indices:
            positions.append(index_to_reference(index, col_index))
    return positions

def list_to_str(input_list):
    string = ""
    for i in range(len(input_list)):
        string = string + input_list[i] + ", "
    return string[:-2]



