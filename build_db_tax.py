
plant_papers = {}
filename = 'unique_results/unique_tax_count_bigger_than_1.txt'
f = open(filename, encoding="utf-8")

list_of_plants = []
lines = f.readlines()
for line in lines:
    line = line.split("\n")[0]
    list = line.split(" ")
    PMC = list[0]
    plant_list = list
    plant_list.pop(0)
    plant_names = ' '.join(plant_list).split(" counts:")[0]
    plants_in_paper = ""

    list_plant_names = plant_names.split(",")
    for name in list_plant_names:
        short_name = name.split("|")[0]
        if short_name not in list_of_plants:
            list_of_plants.append(short_name)
        if short_name not in plants_in_paper:
            if plants_in_paper == "":
                plants_in_paper = short_name
            else:
                plants_in_paper = plants_in_paper + "," + short_name

    if PMC not in plant_papers:
        plant_papers[PMC] = plants_in_paper

miR_plant_papers = []
with open('intersections/mir_tax_papers.txt', 'r') as f:
    lines = f.readlines()
    for pmc in lines:
        miR_plant_papers.append(pmc.strip("\n"))


papers_of_plant = {}
miR_Papers_of_plant = {}

for plant in list_of_plants:
    papers = ""
    miR_papers = ""
    for paper in plant_papers:
        if plant in plant_papers[paper].split(","):
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


with open('myresults/db_mirtax', 'w', encoding="utf-8") as f:
    for line in list_of_plants:
        f.write(line)
        f.write(": " + papers_of_plant[line])
        f.write('\n')

