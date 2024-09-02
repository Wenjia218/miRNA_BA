filename = "textmining_resutls/unique_tax_count_bigger_than_3.txt"
on_topic = {}
f = open(filename, encoding="utf-8")
lines = f.readlines()
for line in lines:
    PMC = line.split(" ")[0]
    first_position = line.split("|")[1].split(",")[0]
    if int(first_position[0]) < 3:
        on_topic[PMC] = line


strick_papers = []
filename2 = "intersections/strick_mir_tax_papers.txt"
f2 = open(filename2, encoding="utf-8")
lines2 = f2.readlines()
for line2 in lines2:
    line2 = line2.strip("\n")
    strick_papers.append(line2)

output = {}
for PMC in on_topic:
    if PMC in strick_papers:
        output[PMC] = on_topic[PMC]

with open('textmining_resutls/filtered_mirtax_in_titel_abstract.txt', 'w', encoding="utf-8") as f:
    for PMC in output:
        f.write(output[PMC])




