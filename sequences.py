import random

sequence = {}
filename = "unique_results/unique_results2_withallwords.txt"
counts = {}
papers = []
f = open(filename, encoding="utf-8")
lines = f.readlines()
for line in lines:
    mirnas = line.split(" ")[1]
    list = mirnas.split(",")
    last_item = "unknown"
    for item in list:
        if len(item) > 20:
            if item not in sequence:
                sequence[item] = last_item
            else:
                sequence[item] = sequence[item]  + "," + last_item
            if item not in counts:
                counts[item] = 1
            else:
                counts[item] = counts[item] + 1
            last_item = item
            break
        last_item = item

with open('myresults/seuquences.txt', 'w') as f:
    for key in sequence:
        f.write(key + ": " + sequence[key])
        f.write('\n')