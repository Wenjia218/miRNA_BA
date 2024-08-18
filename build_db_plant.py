
plant_papers = {}
filename = 'unique_results/unique_results_withallwords.txt'
f = open(filename, encoding="utf-8")


list_of_plants = []
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
    list_plant_names = plant_names.split(",")
    for name in list_plant_names:
        if name not in list_of_plants:
            list_of_plants.append(name)

miR_plant_papers = []
with open('intersections/mirna_plant.txt', 'r') as f:
    lines = f.readlines()
    for pmc in lines:
        miR_plant_papers.append(pmc.strip("\n"))



papers_of_plant = {}
miR_Papers_of_plant = {}

for plant in list_of_plants:
    papers = ""
    miR_papers = ""
    for paper in plant_papers:
        if plant in plant_papers[paper]:
            if papers == "":
                papers = papers + paper
            else:
                papers = papers + "," + paper
            if paper in miR_plant_papers:
                if miR_papers == "":
                    miR_papers = paper
                else:
                    miR_papers = miR_papers + "," + paper
    papers_of_plant[plant] = papers
    miR_Papers_of_plant[plant] = miR_papers


with open('myresults/db_plant.txt', 'w', encoding="utf-8") as f:
    for line in list_of_plants:
        f.write(line)
        f.write(": " + papers_of_plant[line])
        f.write('\n')


with open('myresults/db_mirplant.txt', 'w', encoding="utf-8") as f:
    for line in list_of_plants:
        f.write(line)
        f.write(": " + miR_Papers_of_plant[line])
        f.write('\n')