import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


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

'''

possible_lists_sum_score = (possible_lists_df['FORM_score'] + 2 * possible_lists_df['tax_sum'] + 2 * possible_lists_df['mir_sum']).tolist()
relevant_lists_sum_score = (relevant_lists_df['FORM_score'] + 2 * relevant_lists_df['tax_sum'] + 2 * relevant_lists_df['mir_sum']).tolist()
difference_sum_score = (difference_df['FORM_score'] + 2 * difference_df['tax_sum'] + 2 * difference_df['mir_sum']).tolist()
relevant_lists3_sum_score = (relevant_lists3_df['FORM_score'] + 2 * relevant_lists3_df['tax_sum'] + 2 * relevant_lists3_df['mir_sum']).tolist()

sample_size = 3000

# Resample with replacement
difference_resampled = np.random.choice(difference_sum_score, sample_size, replace=True)
relevant_resampled = np.random.choice(relevant_lists_sum_score, sample_size, replace=True)
relevant3_resampled = np.random.choice(relevant_lists3_sum_score, sample_size, replace=True)
possible_resampled = np.random.choice(possible_lists_sum_score, sample_size, replace=True)


# Plot KDE for the resampled lists
sns.kdeplot(difference_resampled, label='Difference Sum Score', linewidth=2)
sns.kdeplot(relevant_resampled, label='Relevant Lists Sum Score', linewidth=2)
sns.kdeplot(relevant3_resampled, label='Relevant Lists 3 Sum Score', linewidth=2)
sns.kdeplot(possible_resampled, label='Possible Lists Sum Score', linewidth=2)

# Add labels and legend
plt.xlabel('sum of scores')
plt.ylabel('Density')
plt.title('Distribution Comparison with Resampled Data')
plt.legend()

output_file = "plot/distribution_of_scores_PMC.png"  # You can change the file name and extension
plt.savefig(output_file, dpi=300, bbox_inches='tight')
plt.show()

'''

# scatterplot

possible_lists_FORM_mir_score = (possible_lists_df['FORM_score'] + 2 * possible_lists_df['mir_sum']).tolist()
relevant_lists_FORM_mir_score = (relevant_lists_df['FORM_score'] + 2 * relevant_lists_df['mir_sum']).tolist()
difference_FORM_mir_score = (difference_df['FORM_score'] + 2 * difference_df['mir_sum']).tolist()
relevant_lists3_FORM_mir_score = (relevant_lists3_df['FORM_score'] + 2 * relevant_lists3_df['tax_sum'] + 2 * relevant_lists3_df['mir_sum']).tolist()


possible_lists_tax_score = (possible_lists_df['tax_sum']).tolist()
relevant_lists_tax_score = (relevant_lists_df['tax_sum']).tolist()
difference_tax_score = (difference_df['tax_sum']).tolist()
relevant_lists3_tax_score = (relevant_lists3_df['tax_sum']).tolist()

# Plot each group with a different color
#plt.scatter(possible_lists_FORM_mir_score, possible_lists_tax_score, color='blue', label='possible_list', alpha=0.5, s=5)
plt.scatter(relevant_lists_FORM_mir_score, relevant_lists_tax_score, color='green', label='relevant_papers', alpha=0.5, s=3)
plt.scatter(difference_FORM_mir_score, difference_tax_score, color='red', label='Filtered-out', alpha=0.5, s=3)
#plt.scatter(relevant_lists3_FORM_mir_score, relevant_lists3_tax_score, color='yellow', label='more relevant papers', alpha=0.5, s=3)

# Add labels, legend, and title
plt.xlabel('sum of FORM and mir scores')
plt.ylabel('tax scores')
#plt.xscale('log')
#plt.yscale('log')
plt.title('The scores of each PMC paper with/without filter')
plt.legend()

# Show the plot
plt.show()