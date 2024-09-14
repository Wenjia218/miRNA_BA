
import random

PMC = []
with open('textmining_resutls/filtered_mirtax_in_titel_abstract.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        PMC.append(line.split(" ")[0])

random.shuffle(PMC)
PMC100 = PMC[:100]
for item in PMC100:
    print(item + "\n")