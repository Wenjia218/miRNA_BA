import glob
import os

files2 = glob.glob("benchmarking/*.csv")

benchmarking = {}

for file in files2:
    with open(file, mode='r') as file:

        lines = file.readlines()
        True_numbers = [0, 0, 0, 0]
        True_percent = []
        number_of_rows = len(lines)

        for line in lines:
            list_of_line = line.split(", ")
            if list_of_line[2] == "True":
                True_numbers[0] = True_numbers[0] + 1
            if list_of_line[3] == "True":
                True_numbers[1] = True_numbers[1] + 1
            if list_of_line[4] == "True":
                True_numbers[2] = True_numbers[2] + 1
            if list_of_line[5] == "True":
                True_numbers[3] = True_numbers[3] + 1
        for i in range(4):
            True_percent.append(True_numbers[i] / number_of_rows)
        benchmarking[file.name.strip(".csv").strip("benchmarking").strip("\\")] = True_percent

print(benchmarking)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame([['carrot_miRNA', 'tax in t/a', 0.8824], ['carrot_miRNA', 'tax > 3', 1.0], ['carrot_miRNA', 'FORM in t/a', 0.3529], ['carrot_miRNA', 'FORM > 3', 0.5882],
                   ['rice_miRNA', 'tax in t/a', 0.8], ['rice_miRNA', 'tax > 3', 0.8], ['rice_miRNA', 'FORM in t/a', 0.8], ['rice_miRNA', 'FORM > 3', 0.8],
                   ['tomato_miRNA', 'tax in t/a', 0.9444], ['tomato_miRNA', 'tax > 3', 0.9444], ['tomato_miRNA', 'FORM in t/a', 0.7222], ['tomato_miRNA', 'FORM > 3', 0.9444]], columns=['group','column','val'])

# plot with seaborn barplot
sns.barplot(data=df, x='column', y='val', hue='group')
plt.show()