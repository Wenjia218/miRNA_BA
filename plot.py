import math

import seaborn as sns
import matplotlib.pyplot as plt

counts = {}

with open('myresults/db_paper_counts.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        list = line.split(": ")
        seq = list[0]
        count = int(list[1])
        counts[seq] = count

plt.hist(counts.values(), bins=100, edgecolor='black')
plt.title('counts of PMC paper of each unique sequence')
plt.xlabel('counts with log')
plt.ylabel('Frequency')
plt.show()

def sort_dict_by_values(input_dict):
    sorted_items = sorted(input_dict.items(), key=lambda item: item[1], reverse=True)
    sorted_dict = dict(sorted_items)
    return sorted_dict

print(sort_dict_by_values(counts))