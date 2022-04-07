import json
import numpy as np
import csv

data = np.load('simplified-recipes-1M.npz', allow_pickle=True)
lst = data.files

for ingr in data['ingredients']:
    print(ingr)

header = ['Title', 'Ingredient']

with open("recipes.json", 'r') as f:
    json_data = json.load(f)

# data = ['Afghanistan', 652090, 'AF', 'AFG']

with open('recipes.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    for recipe in json_data['recipes']:
        for ingr in data['ingredients']:
            for ingr_list in recipe['ingredients']:
                if len(ingr) > 2 and ingr in ingr_list:
                    # print(ingr)
                    csv_data = [recipe['title'], ingr]
                    print(csv_data)
                    writer.writerow(csv_data)
