
import matplotlib.pyplot as plt
import numpy as np

counts1 = {}
filename = 'syn/ncbitaxon.33090.syn'
f = open(filename, encoding="utf-8")
lines = f.readlines()
for line in lines:
    list = line.split(":")
    PMC = list[0]
    count = len(list[1].split("|"))
    counts1[PMC] = count


counts2 = {}
filename = 'syn/ncbitaxon.33090_itis.syn'
f = open(filename, encoding="utf-8")
lines = f.readlines()
for line in lines:
    list = line.split(":")
    PMC = list[0]
    count = len(list[1].split("|"))
    counts2[PMC] = count


plt.hist(counts1.values(), color='red', bins=80, alpha=0.65)
plt.hist(counts2.values(), color='deepskyblue', bins=80, alpha=0.65)
plt.title('frequency of counts of synonyms of each objetct')
plt.xlabel('counts of synonyms')
plt.ylabel('Frequency with log')
plt.yscale('log')
plt.show()
