
plant_papers = {}
filename = 'unique_results/unique_results.txt'
f = open(filename, encoding="utf-8")
lines = f.readlines()
for line in lines:
    list = line.split(" ")
    PMC = list[0]
    if PMC not in plant_papers:
        plant_papers[PMC] = line

mirna_papers = {}
with open('unique_results/unique_results2.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        list = line.split(" ")
        PMC = list[0]
        if PMC not in mirna_papers:
            mirna_papers[PMC] = line

MIR_papers = {}
with open('unique_results/unique_results3.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        list = line.split(" ")
        PMC = list[0]
        if PMC not in MIR_papers:
            MIR_papers[PMC] = line
inter = {}
for PMC in plant_papers:
    if PMC in MIR_papers:
        inter[PMC] = plant_papers[PMC] + "/" + MIR_papers[PMC]

inter2 = {}
for PMC in MIR_papers:
    if PMC in mirna_papers:
        inter2[PMC] = MIR_papers[PMC] + "/" + mirna_papers[PMC]

inter3 = {}
for PMC in mirna_papers:
    if PMC in plant_papers:
        inter3[PMC] = mirna_papers[PMC] + "/" + plant_papers[PMC]


with open('intersections/plant_Form.txt', 'w') as f:
    for PMC in inter:
        f.write(PMC)
        f.write('\n')

with open('intersections/FORM_mirna.txt', 'w') as f:
    for PMC in inter2:
        f.write(inter2[PMC])
        f.write('\n')

with open('intersections/mirna_plant.txt', 'w') as f:
    for PMC in inter3:
        f.write(PMC)
        f.write('\n')