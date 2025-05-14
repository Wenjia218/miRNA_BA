#Gibt es eine Idee wieviele miRNA in der Literatur beschrieben sind im Vergleich zu den schon bekannten?
##Vlt das gleiche Beispiel von oben: xx sind bekannt (aus Genome, Sequenzierung, ...) wieviele sind tatssächlich in der
#literatur beschrieben und durch Text mining gefunden?

import matplotlib.pyplot as plt

bekannt_miRNA = {}
filename = 'syn/mirna_new_no3p5p.syn'
f = open(filename, encoding="utf-8")
lines = f.readlines()
for line in lines:
    line = line.strip("\n")
    bekannt_miRNA[line.split(": ")[0]] = line.split(": ")[1].split("|")

# bekannt miRNA: 41606 (different sequence)
print(len(bekannt_miRNA))

synonym_object = {}
for seq in bekannt_miRNA:
    for synonym in bekannt_miRNA[seq]:
        synonym_object[synonym.lower()] = seq


literature_miRNA = []
textmining_results = {}
filename = 'textmining_results/PMC_mir_withallwords'
f = open(filename, encoding="utf-8")
lines = f.readlines()
for line in lines:
    textmining_results[line.split(": ")[0]] = line.split(": ")[1]


for PMC in textmining_results:
    synonyms = textmining_results[PMC]
    for synonym in synonyms.split(","):
        mir = synonym.split("|")[0]
        if mir.lower() in synonym_object:
            seq = synonym_object[mir.lower()]
            if seq not in literature_miRNA:
                literature_miRNA.append(seq)

print(literature_miRNA)
print(len(literature_miRNA))  # 16898

species_codes = ['known miRNA', 'miRNA in literatures']
literature_counts = [41606, 16898]

# Create the bar plot
plt.figure(figsize=(10, 6))
plt.bar(species_codes, literature_counts, color='lightcoral')


plt.xlabel('')
plt.ylabel('counts of different miRNA sequences')
plt.title('Comparison of Database-Known miRNAs vs. Studied miRNAs in PMC Papers')

# Show the plot
plt.show()
