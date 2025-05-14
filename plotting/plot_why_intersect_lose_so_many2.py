import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import re

def calculate_min_distance(position_column1, position_column2):
    position_list1 = position_column1.tolist()
    position_list2 = position_column2.tolist()

    min_distances = []
    for i in range(len(position_list1)):
        position1 = position_list1[i]
        position2 = position_list2[i]
        min_dis = 1000
        if type(position1) != list or type(position2) != list:
            continue
        for item1 in position1:
            for item2 in position2:
                distance = abs(int(item1.split(".")[1]) - int(item2.split(".")[1]))
                if distance < min_dis:
                    min_dis = distance

        min_distances.append(min_dis)
    return min_distances


df = pd.read_csv("myresults/dataframe_alltextmining.csv")

possible_lists = []
f = open("intersections/PMC_possible_lists", encoding="utf-8")
lines = f.readlines()
for line in lines:
    possible_lists.append(line.strip("\n"))

relevant_lists = []
f = open("intersections/PMC_relevant_lists", encoding="utf-8")
lines = f.readlines()
for line in lines:
    relevant_lists.append(line.strip("\n"))

relevant_lists3 = []
f = open("intersections/PMC_relevant_lists3", encoding="utf-8")
lines = f.readlines()
for line in lines:
    relevant_lists3.append(line.strip("\n"))

difference = list(set(possible_lists) - set(relevant_lists))

possible_lists_df = df[df['PMC'].isin(possible_lists)]
relevant_lists_df = df[df['PMC'].isin(relevant_lists)]
relevant_lists3_df = df[df['PMC'].isin(relevant_lists3)]
difference_df = df[df['PMC'].isin(difference)]

dataframes = [possible_lists_df, relevant_lists_df, relevant_lists3_df, difference_df]  # List of DataFrames

# Process each DataFrame
for i, df in enumerate(dataframes):
    df['FORM_extracted_numbers'] = df['FORM_results'].str.findall(r'\|([\d.]+)')
    df['tax_extracted_numbers'] = df['tax_results'].str.findall(r'\|([\d.]+)')
    df['mir_extracted_numbers'] = df['mir_results'].str.findall(r'\|([\d.]+)')


possible_lists_distances = calculate_min_distance(possible_lists_df['FORM_extracted_numbers'], possible_lists_df['tax_extracted_numbers'])
relevant_lists_distances = calculate_min_distance(relevant_lists_df['FORM_extracted_numbers'], relevant_lists_df['tax_extracted_numbers'])
difference_distances = calculate_min_distance(difference_df['FORM_extracted_numbers'], difference_df['tax_extracted_numbers'])
relevant_lists3_distances = calculate_min_distance(relevant_lists3_df['FORM_extracted_numbers'], relevant_lists3_df['tax_extracted_numbers'])

sample_size = 3000

# Resample with replacement
difference_resampled = np.random.choice(difference_distances, sample_size, replace=True)
relevant_resampled = np.random.choice(relevant_lists_distances, sample_size, replace=True)
relevant3_resampled = np.random.choice(relevant_lists3_distances, sample_size, replace=True)
possible_resampled = np.random.choice(possible_lists_distances, sample_size, replace=True)

# Plot KDE for the resampled lists
sns.kdeplot(difference_resampled, label='possible - relevant list', linewidth=2)
sns.kdeplot(relevant_resampled, label='relevant list', linewidth=2)
sns.kdeplot(relevant3_resampled, label='relevant list3', linewidth=2)
sns.kdeplot(possible_resampled, label='possible list', linewidth=2)

# Add labels and legend
plt.xlabel('distance (sentence)')
plt.ylabel('Density')
plt.title('Distribution Comparison with Resampled Data of min distances')
plt.legend()

output_file = "plot/distribution_of_distances_PMC.png"  # You can change the file name and extension
plt.savefig(output_file, dpi=300, bbox_inches='tight')
plt.show()
