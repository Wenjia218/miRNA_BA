
plant_papers = {}
list_of_plants = []

filename = 'myresults/db_plant.txt'
f = open(filename, encoding="utf-8")
lines = f.readlines()
for line in lines:
    plant_papers[line.split(":")[0]] = line.split(":")[1]


for name in plant_papers:
    if name not in list_of_plants:
        list_of_plants.append(name)


mirna_papers = {}
with open('unique_results/unique_results2_withallwords.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        list = line.split(" ")
        PMC = list[0]
        key = list[1]
        if PMC not in mirna_papers:
            mirna_papers[PMC] = key

plant_mir = {}
for plant in list_of_plants:
    list_of_papers = plant_papers[plant].split(",")
    for paper in list_of_papers:
        if paper in mirna_papers:
            mirs = mirna_papers[paper]
            if plant not in plant_mir:
                plant_mir[plant] = mirs
            else:
                plant_mir[plant] = plant_mir[plant] + "," + mirs

print(plant_mir["Solanum lycopersicum"])

with open('myresults/plant_mir.txt', 'w', encoding="utf-8") as f:
    for plant in plant_mir:
        f.write(plant)
        f.write(": " + plant_mir[plant])
        f.write('\n')