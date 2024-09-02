
plant_papers = {}
filename = 'unique_results/unique_tax_count_bigger_than_3.txt'
f = open(filename, encoding="utf-8")
lines = f.readlines()
for line in lines:
    list = line.split(" ")
    PMC = list[0]
    if PMC not in plant_papers:
        plant_papers[PMC] = line

FORM_counts = {}
FORM_positions = {}
with open('unique_results/unique_FORM_withallwords.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        PMC = line.split(" ")[0]
        count = line.split("counts: ")[1]
        print(line)
        position = line.split("|")[1].split(",")[0]
        if PMC not in FORM_counts:
            FORM_counts[PMC] = count
        if PMC not in FORM_positions:
            FORM_positions[PMC] = position


inter = []
for PMC in plant_papers:
    if PMC in FORM_counts and int(FORM_positions[PMC][0]) < 3:
        inter.append(PMC)
'''
inter2 = []
for PMC in plant_papers:
    if PMC in FORM_counts and int(FORM_positions[PMC][0]) < 3:
        inter2.append(PMC)
'''

with open('intersections/strick_mir_tax_papers.txt', 'w') as f:
    for PMC in inter:
        f.write(PMC)
        f.write('\n')

'''
with open('intersections/strick_mir_plant_papers.txt', 'w') as f:
    for PMC in inter2:
        f.write(PMC)
        f.write('\n')
'''