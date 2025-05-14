
#was sind die Species mit den meisten bekannten miRNA? Top 10 vielleicht auch als iTol und upset
#Wie sieht es mit bekannten Nahrungsmittelpflanzen aus (möhre, Tomate, Kartoffel irgendein schönes Beispiel
#wo man zig miRNA hat. Wie ist da der Überlapp mit den ca 2500 Human und/oder xxx Maus miRNA ?
#Wieviele sind vermutlich xenomirs? (vlt so ein Venn Diagramm ?)


import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

import re

counts1 = {}
filename = 'syn/mirna_new_no3p5p.syn'
f = open(filename, encoding="utf-8")
lines = f.readlines()
for line in lines:
    line = line.strip("\n")
    list_PMC = line.split(": ")
    PMC = list_PMC[0]
    syns = list_PMC[1].split("|")[2:]
    counts1[PMC] = "|".join(syns)


pattern = r"(\w{3})(?=-mir|-let|-bantam)"
counts_species = {}

species_mir = {}
human_mir = []
# Find all matches
for seq in counts1:
    matches = re.findall(pattern, counts1[seq], re.IGNORECASE)
    for specie in matches:
        if specie == "hsa" and seq not in human_mir:
            human_mir.append(seq)
        if specie not in species_mir:
            species_mir[specie] = seq
        else:
            if seq not in species_mir[specie]:
                species_mir[specie] = species_mir[specie] + "," + seq

    count = len(set(matches))
    if count == 0:
        count = 1
    counts_species[seq] = count


human_mir_in_mirsyn = {}
specie_codes = []
for seq in counts1:
    if seq in human_mir:
        human_mir_in_mirsyn[seq] = counts1[seq]
        pattern = r"\b[a-z]{3}-(?:miR|let)-[a-zA-Z0-9]+\b"
        # Find all matches
        matches = re.findall(pattern, counts1[seq])
        # Print the results
        for match in matches:
            code = match.split("-")[0]
            if code not in specie_codes:
                specie_codes.append(code)



# Extract only the counts
values = list(counts_species.values())

# Count the frequency of each count value
count_frequencies = Counter(values)

# Extract data for plotting
unique_counts = list(count_frequencies.keys())
frequencies = list(count_frequencies.values())

species_mir_count = {}
for specie in species_mir:
    species_mir_count[specie] = len(species_mir[specie].split(","))

sorted_species_mir_count = dict(sorted(species_mir_count.items(), key=lambda item: item[1], reverse=True))
print(sorted_species_mir_count)

'''
# Plot the data
plt.hist(values, bins=10, color='skyblue', edgecolor='black')  # Adjust bins as needed
plt.xlabel('Counts of different spezies where the miRNA was found')
plt.ylabel('Frequency with log')
plt.yscale('log')
plt.title('Histogram of spezies counts per miRNA')
plt.show()

# Sort dictionary by values and take the top 10
top_sequences = dict(sorted(counts_species.items(), key=lambda x: x[1], reverse=True)[:10])
keys = list(top_sequences.keys())
values = list(top_sequences.values())

# Plot truncated bar chart
plt.bar(keys, values, color='skyblue', edgecolor='black')
plt.xticks(rotation=90, fontsize=10)
plt.xlabel('Top Sequences', fontsize=12)
plt.ylabel('Counts of species where the miRNAs were found', fontsize=12)
plt.title('Top 10 Sequence Counts', fontsize=14)
plt.tight_layout()
plt.show()



import matplotlib.pyplot as plt

# Data for plotting
species_codes = ['hsa', 'mmu', 'gga', 'mdo', 'bta', 'mml', 'rno', 'eca', 'oni', 'cpo']
literature_counts = [2618, 1955, 1230, 1124, 1021, 906, 759, 686, 681, 656]
species_names = [
    "Homo sapiens (Human)",
    "Mus musculus (Mouse)",
    "Gallus gallus (Chicken)",
    "Monodelphis domestica (Opossum)",
    "Bos taurus (Cow)",
    "Macaca mulatta (Rhesus macaque)",
    "Rattus norvegicus (Rat)",
    "Equus caballus (Horse)",
    "Oreochromis niloticus (Nile tilapia)",
    "Capra hircus (Goat)"
]


# Create the bar plot
plt.figure(figsize=(10, 6))
plt.bar(species_names, literature_counts, color='lightcoral')
plt.xlabel('Species Codes')
plt.xticks(rotation=90)
plt.ylabel('miRNA counts')
plt.title('found miRNA counts of each specie')
plt.tight_layout()

# Show the plot
plt.show()
'''
