
import matplotlib.pyplot as plt
import numpy as np

counts1 = {}
filename = 'myresults/FORM_bigger3_tax_in_ta_withdate.txt'
f = open(filename, encoding="utf-8")
lines = f.readlines()
for line in lines:
    list = line.split(" ")
    PMC = list[0]
    year = list[1].strip("\n")
    print(year)
    if year != "1":
        counts1[PMC] = year



plt.hist(counts1.values(), color='blue', bins=80, alpha=0.65)
plt.title('counts of articles published on PMC annually on plant miRNAs')
plt.xlabel('year')
plt.ylabel('counts of articles')
#plt.yscale('log')
plt.show()
