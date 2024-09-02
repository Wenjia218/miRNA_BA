import math

plant_papers = {}
filename = 'textmining_resutls/unique_results_withallwords.txt'
f = open(filename, encoding="utf-8")

lines = f.readlines()
for line in lines:
    line = line.split("\n")[0]
    list = line.split(" ")
    PMC = list[0]
    plant_names = list
    plant_names.pop(0)
    plant_names.pop(len(plant_names) - 1)
    plant_names = ' '.join(plant_names)
    if PMC not in plant_papers:
        plant_papers[PMC] = plant_names

'''
MIR_papers = []
with open('textmining_resutls/unique_results3.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        list = line.split(" ")
        PMC = list[0]
        if PMC not in MIR_papers:
            MIR_papers.append(PMC)
'''

counts = {}
for key in plant_papers:
    plant_names = plant_papers[key].split(",")
    for plant_name in plant_names:
        if plant_name not in counts:
            counts[plant_name] = 0
        else:
            counts[plant_name] = counts[plant_name] + 1

'''
counts2 = {}
for key in plant_papers:
    if key in MIR_papers:
        plant_names = plant_papers[key].split(",")
        for plant_name in plant_names:
            if plant_name not in counts2:
                counts2[plant_name] = 1
            else:
                counts2[plant_name] = counts2[plant_name] + 1
'''

def get_key(val, my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key

    return "key doesn't exist"

def sort_dict_by_values(input_dict):
    sorted_items = sorted(input_dict.items(), key=lambda item: item[1], reverse=True)
    sorted_dict = dict(sorted_items)
    return sorted_dict

order_counts = sort_dict_by_values(counts)
with open('myresults/plant_counts.txt', 'w', encoding="utf-8") as f:
    for plant in order_counts:
        f.write(plant + " " + str(order_counts[plant]))
        f.write('\n')

'''
order_counts2 = sort_dict_by_values(counts2)
with open('myresults/mir_plant_counts.txt', 'w', encoding="utf-8") as f:
    for plant in order_counts2:
        f.write(plant + " " + str(order_counts2[plant]))
        f.write('\n')


top_10 = sorted(counts.values(), reverse=True)[0:19]
top_10_keys = []
for value in top_10:
    top_10_keys.append(get_key(value, counts)[0] + "." + get_key(value, counts).split(" ")[1])

top_10_MIR = sorted(counts2.values(), reverse=True)[0:19]
top_10_MIR_keys = []
for value in top_10_MIR:
    top_10_MIR_keys.append(get_key(value, counts2)[0] + "." + get_key(value, counts2).split(" ")[1])

import matplotlib.pyplot as plt

plt.hist(counts.values(), bins=50)
plt.yscale('log')
plt.gca().set(title='Frequency Histogram of counts of plants appear in PMC', ylabel='Frequency')
plt.show()

plt.bar(top_10_keys, top_10)
plt.xticks(rotation=45, ha='right')
plt.savefig("plot/topplants.png")

plt.bar(top_10_MIR_keys, top_10_MIR)
plt.xticks(rotation=45, ha='right')
plt.savefig("plot/topplantsofmirna.png")
'''