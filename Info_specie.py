import json

plant_papers = {}
list_of_plants = []

filename = 'my_results/db_mirplant.txt'
f = open(filename, encoding="utf-8")
lines = f.readlines()
for line in lines:
    plant_papers[line.split(":")[0]] = line.split(":")[1]


for name in plant_papers:
    if name not in list_of_plants:
        list_of_plants.append(name)


plant_mir = {}
with open('my_results/plant_mir.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        list = line.split(": ")
        plant = list[0]
        miRs = list[1]
        if plant not in plant_mir:
            plant_mir[plant] = miRs

def sort_dict_by_values(input_dict):
    sorted_items = sorted(input_dict.items(), key=lambda item: item[1], reverse=True)
    sorted_dict = dict(sorted_items)
    return sorted_dict


miR_list = plant_mir["Solanum lycopersicum"].split(",")
paper_list = plant_papers["Solanum lycopersicum"].split(",")
counts = {}
for item in miR_list:
    item = item.strip("\n")
    if item not in counts:
        counts[item] = 1
    else:
        counts[item] = counts[item] + 1

counts = sort_dict_by_values(counts)
sum = 0
for i in counts:
    sum = sum + counts[i]


with open('examples/tomato.txt', 'w', encoding="utf-8") as f:
        f.write("Solanum lycopersicum")
        f.write(": " + "\n")
        f.write("Summary: counts of miRs " + str(len(miR_list)) + ", counts of papers " +str(len(paper_list)))
        f.write("\n")
        f.write("A distribution of miRNAs: ")
        f.write("\n")
        f.write(json.dumps(counts))
        f.write("\n")
        f.write(plant_mir["Solanum lycopersicum"])
        f.write('\n')
        f.write(plant_papers["Solanum lycopersicum"])