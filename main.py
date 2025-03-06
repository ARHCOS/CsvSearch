import os
from scripts.functions import *
import pandas as pd

csv_folder = get_current_dir() + "\\CSV"

csv_files = get_csv_files(os.listdir(csv_folder))

search_str = input("Input your search : ")

with open(get_current_dir()+"\\results.txt", 'w') as file:
    file.write(f"Results for \"{search_str}\" :\n")
    file.write("\n")
    file.write("\n")
    match = 0
    for i in range(len(csv_files)):
        dataframe = pd.read_csv(csv_folder + "\\" + csv_files[i])
        results = find_positions(dataframe, search_str)
        match = match + len(results)
        if len(results) > 0:
            lenght = len(results)
            file.write(f"Found {lenght} results in {csv_files[i]} in : " + list_to_str(results) + "\n")
            file.write("\n")
input(f"Printed {match} match in results.txt")