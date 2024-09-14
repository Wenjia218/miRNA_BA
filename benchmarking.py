plant_papers = {}
filename = 'textmining_resutls/unique_tax_itis.txt'
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
with open('textmining_resutls/unique_FORM_withallwords.txt', 'r') as f:
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
    print('Enter PMCID: print "end" to end script')
    PMCID = input()
    if PMCID == "end":
        break
    elif PMCID.startswith("PMC"):
        list_PMCIDs.append(PMCID)
    else:
        print("Wrong input")
        break

output_lines = {}
for PMC in plant_papers:
    for PMC2 in list_PMCIDs:
        if PMC == PMC2:
            output_lines[PMC] = plant_papers[PMC]

for PMC in FORM_papers:
    for PMC2 in list_PMCIDs:
        if PMC == PMC2:
            output_lines[PMC] = output_lines[PMC] + "   " + FORM_papers[PMC]
            print(output_lines[PMC])



import csv

with open('benchmarking.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for PMC in output_lines:
        write_list = []
        write_list.append(PMC + ",")
        write_list.append(output_lines[PMC].replace("|", ""))
        spamwriter.writerow(write_list)



