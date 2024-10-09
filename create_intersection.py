
plant_papers_in_topic_abstract = {}
filename = 'textmining_results/unique_tax_itis_in_topic_or_abstract'
f = open(filename, encoding="utf-8")
lines = f.readlines()
for line in lines:
    list = line.split(" ")
    PMC = list[0]
    if PMC not in plant_papers_in_topic_abstract:
        plant_papers_in_topic_abstract[PMC] = line

plant_papers_bigger_3 = {}
filename = 'textmining_results/unique_tax_itis_count_bigger_than_3'
f = open(filename, encoding="utf-8")
lines = f.readlines()
for line in lines:
    list = line.split(" ")
    PMC = list[0]
    if PMC not in plant_papers_bigger_3:
        plant_papers_bigger_3[PMC] = line

FORM_papers_in_topic_abstract = {}
with open('textmining_results/unique_FORM_in_topic_or_abstract', 'r') as f:
    lines = f.readlines()
    for line in lines:
        list = line.split(" ")
        PMC = list[0]
        if PMC not in FORM_papers_in_topic_abstract:
            FORM_papers_in_topic_abstract[PMC] = line

FORM_papers_bigger_3 = {}
with open('textmining_results/unique_FORM_count_bigger_than_3', 'r') as f:
    lines = f.readlines()
    for line in lines:
        list = line.split(" ")
        PMC = list[0]
        if PMC not in FORM_papers_bigger_3:
            FORM_papers_bigger_3[PMC] = line


inter1 = []
for PMC in plant_papers_in_topic_abstract:
    if PMC in FORM_papers_in_topic_abstract:
        inter1.append(PMC)

inter2 = []
for PMC in plant_papers_in_topic_abstract:
    if PMC in FORM_papers_bigger_3:
        inter2.append(PMC)

inter3 = []
for PMC in plant_papers_bigger_3:
    if PMC in FORM_papers_in_topic_abstract:
        inter3.append(PMC)

inter4 = []
for PMC in plant_papers_bigger_3:
    if PMC in FORM_papers_bigger_3:
        inter4.append(PMC)


with open('intersections/FORM_in_topic_abstract_tax_itis_in_topic_abstract.txt', 'w') as f:
    for PMC in inter1:
        f.write(PMC)
        f.write('\n')


with open('intersections/FORM_bigger3_tax_itis_in_topic_abstract.txt', 'w') as f:
    for PMC in inter2:
        f.write(PMC)
        f.write('\n')

with open('intersections/FORM_in_topic_abstract_tax_itis_bigger3.txt', 'w') as f:
    for PMC in inter3:
        f.write(PMC)
        f.write('\n')


with open('intersections/FORM_in_topic_abstract_tax_itis_in_topic_abstract.txt', 'w') as f:
    for PMC in inter4:
        f.write(PMC)
        f.write('\n')