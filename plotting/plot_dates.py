
'''

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

'''


import glob

files2 = glob.glob("timelines/*intopic.txt")

tax_years = {}
for file in files2:
    with open(file, mode='r', encoding="utf-8") as file:
        lines = file.readlines()
        years = []
        for line in lines:
            if line.startswith("PMC"):
                year = line.split(": ")[1].split(",")[0]
                years.append(year)

        tax_years[file.name.split("timeline_")[1].split(".txt")[0]] = years

x_axis = []
for i in range(25):
    if len(str(i)) == 1:
        x_axis.append("200" + str(i))
    else:
        x_axis.append("20" + str(i))


counts_of_years = {}
for tax in tax_years:
    dic_years = {}
    for year in x_axis:
        dic_years[year] = 0
    for year2 in tax_years[tax]:
        dic_years[year2] = dic_years[year2] + 1

    counts_of_years[tax] = list(dic_years.values())

import matplotlib.pyplot as plt
# Create the plot
plt.figure(figsize=(8, 6))     # Set the figure size

# Plot each line
for tax in counts_of_years:
    plt.plot(x_axis, counts_of_years[tax], label=tax, marker='o')  # Line 1: Red with circle markers


# Add title and labels
plt.title('counts of PMC papers (with tax in topic) per year for different organisms')
plt.xlabel('year')
plt.ylabel('counts')

# Add grid for clarity
plt.grid(True)

# Display the legend to differentiate the lines
plt.legend()

# Show the plot
plt.show()



