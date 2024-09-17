# structure of csv
# PMCID, Value, if tax in topic/abstract, if tax > 3, if FORM in topic/abstract, if FORM > 3 times, all found syns and positions.....

plant_papers = {}
filename = 'textmining_results/unique_tax_itis.txt'
f = open(filename, encoding="utf-8")
lines = f.readlines()
for line in lines:
    list = line.split(" ")
    PMC = list[0]

    list.pop(0)
    line2 = ''.join(list)

    if PMC not in plant_papers:
        plant_papers[PMC] = line2.split("count")[0]

FORM_papers = {}
with open('textmining_results/unique_FORM_withallwords.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        list = line.split(" ")
        PMC = list[0]

        list.pop(0)
        line2 = ''.join(list)

        if PMC not in FORM_papers:
            FORM_papers[PMC] = line2.split("count")[0]


list_PMCIDs = []

while True:
    print('Enter PMCID or multiple PMCID split by ,: print "end" to end input')
    PMCID = input()
    if PMCID == "end":
        break
    elif PMCID.startswith("PMC"):
        if len(PMCID.split(",")) == 1:
            list_PMCIDs.append(PMCID)
        else:
            for PMC in PMCID.split(","):
                list_PMCIDs.append(PMC)
    else:
        print("Wrong input")


plant_lines = {}
if_tax_topic_abstract = {}
if_tax_bigger_three = {}
for PMC in plant_papers:
    for PMC2 in list_PMCIDs:
        if PMC == PMC2:
            plant_lines[PMC] = plant_papers[PMC]
            if int(plant_papers[PMC].split(",")[0].split("|")[1][0]) < 3:
                if_tax_topic_abstract[PMC] = True
            else:
                if_tax_topic_abstract[PMC] = False
            if len(plant_papers[PMC].split(",")) > 3:
                if_tax_bigger_three[PMC] = True
            else:
                if_tax_bigger_three[PMC] = False


FORM_lines = {}
if_FORM_topic_abstract = {}
if_FORM_bigger_three = {}
for PMC in FORM_papers:
    for PMC2 in list_PMCIDs:
        if PMC == PMC2:
            FORM_lines[PMC] = FORM_papers[PMC]
            if int(FORM_papers[PMC].split(",")[0].split("|")[1][0]) < 3:
                if_FORM_topic_abstract[PMC] = True
            else:
                if_FORM_topic_abstract[PMC] = False
            if len(FORM_papers[PMC].split(",")) > 3:
                if_FORM_bigger_three[PMC] = True
            else:
                if_FORM_bigger_three[PMC] = False

import csv

with open('benchmarking.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ')
    for PMC in list_PMCIDs:
        write_list = []
        write_list.append(PMC + ",")
        write_list.append("unknown" + ",")
        if PMC in plant_lines:
            write_list.append(str(if_tax_topic_abstract[PMC]) + ",")
            write_list.append(str(if_tax_bigger_three[PMC]) + ",")
        else:
            write_list.append("False" + ",")
            write_list.append("False" + ",")
        if PMC in FORM_lines:
            write_list.append(str(if_FORM_topic_abstract[PMC]) + ",")
            write_list.append(str(if_FORM_bigger_three[PMC]) + ",")
        else:
            write_list.append("False" + ",")
            write_list.append("False" + ",")
        if PMC in plant_lines:
            write_list.append(plant_lines[PMC].replace("|", "") + ",")
        if PMC in FORM_lines:
            write_list.append(FORM_lines[PMC].replace("|", "") + ",")

        print(write_list)
        spamwriter.writerow(write_list)



