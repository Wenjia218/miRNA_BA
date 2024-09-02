mirna_papers = {}
with open('textmining_resutls/unique_results2_withallwords.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        list = line.split(" ")
        PMC = list[0]
        key = list[1]
        if PMC not in mirna_papers:
            mirna_papers[PMC] = key

plant_papers = []
filename = 'textmining_resutls/unique_results_withallwords.txt'
f = open(filename, encoding="utf-8")
lines = f.readlines()
for line in lines:
    list = line.split(" ")
    PMC = list[0]
    if PMC not in plant_papers:
        plant_papers.append(PMC)

counts = {}
for key in mirna_papers:
    mir_name = mirna_papers[key]
    list_of_mir = mir_name.split(",")
    for mir in list_of_mir:
        if mir not in counts:
            counts[mir] = 1
        else:
            counts[mir] = counts[mir] + 1

counts2 = {}
for key in mirna_papers:
    if key in plant_papers:
        mir_name = mirna_papers[key]
        list_of_mir = mir_name.split(",")
        for mir in list_of_mir:
            if mir not in counts2:
                counts2[mir] = 1
            else:
                counts2[mir] = counts2[mir] + 1

def get_key(val, my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key

    return "key doesn't exist"


top_10 = sorted(counts.values(), reverse=True)[0:19]
top_10_keys = []
for value in top_10:
    top_10_keys.append(get_key(value, counts))

print(top_10)
print(top_10_keys)

top_10_plant = sorted(counts2.values(), reverse=True)[0:19]
top_10_plant_keys = []
for value in top_10_plant:
    top_10_plant_keys.append(get_key(value, counts2))

print(top_10_plant)
print(top_10_plant_keys)

import matplotlib.pyplot as plt

#plt.hist(counts.values(), bins=50)
#plt.yscale('log')
#plt.gca().set(title='Frequency Histogram of counts of miRNA appear in PMC', ylabel='Frequency')
#plt.show()

plt.bar(top_10_keys, top_10)
plt.xticks(rotation=45, ha='right')
plt.savefig("plot/topmirna.png")

plt.bar(top_10_plant_keys, top_10_plant)
plt.xticks(rotation=45, ha='right')
plt.show()
#plt.savefig("plot/topmirnainplant.png")