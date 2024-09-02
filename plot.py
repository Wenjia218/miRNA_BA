import math

import seaborn as sns
import matplotlib.pyplot as plt

counts = {}
filename = 'myresults/db_mirplant.txt'
f = open(filename, encoding="utf-8")
lines = f.readlines()
for line in lines:
    list = line.split(": ")
    PMC = list[0]
    count = len(list[1].split(","))
    counts[PMC] = count


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



'''
plt.hist(counts.values(), bins=100, edgecolor='black')
plt.title('frequency of tax syns in papers')
plt.xlabel('counts with log')
plt.ylabel('Frequency')
plt.show()
'''