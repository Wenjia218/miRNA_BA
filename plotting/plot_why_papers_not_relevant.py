import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('benchmarking/PMC_difference_lists_all.csv')
count_PMC = []
other_PMC = []
low_tax = []
low_mir = []
counts = 0
for index, row in df.iterrows():
    print(row['tax_results'])
    if "flag" in row['tax_results'].lower() or "alexa" in row['tax_results'].lower() or "microbiota" in row['tax_results'].lower() or "laser" in row['tax_results'].lower() or "codon" in row['tax_results'].lower() or "california" in row['tax_results'].lower():
        print(row)
        counts = counts + 1
        count_PMC.append(row['PMC'])
    else:
        other_PMC.append(row['PMC'])
        if row['tax_sum'] < 10 and row['mir_sum'] > 10:
            low_tax.append(row['PMC'])
        if row['mir_sum'] < 10 and row['tax_sum'] > 10:
            low_mir.append(row['PMC'])

#filtered_df = df[df['PMC'].isin(count_PMC)]
#filtered_df.to_csv("benchmarking/PMC_difference_others_lists_all.csv", index=False)
print(f"low tax {len(low_tax)}")
print(f"low mir {len(low_mir)}")
print(len(other_PMC))
other_df = df[df['PMC'].isin(other_PMC)]
other_df.to_csv("benchmarking/PMC_difference_find_reason_lists_all.csv", index=False)

names = ["possible PMC", "misleading words", "low plant", "low miRNA", "relevant papers"]
values = [103092, len(count_PMC), len(low_tax), len(low_mir), 20975]

plt.figure(figsize=(10, 6))
plt.bar(names, values, color='lightcoral')
#plt.xlabel('groups')
plt.xticks(rotation=90)
plt.ylabel('count of PMC papers')
plt.title('why 80% papers are not relevant')
plt.tight_layout()

# Show the plot
plt.show()
