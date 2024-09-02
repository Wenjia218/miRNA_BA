# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 15:27:11 2024

@author: admin
"""

import pandas as pd
import re
from tqdm import tqdm
from collections import defaultdict
import os


# data = pd.read_csv("C:/Users/admin/Desktop/wenjia/unique_tax_count_bigger_than_1.txt")

# with open("C:/Users/admin/Desktop/wenjia/unique_tax_count_bigger_than_1.txt", 'r') as file:
#     content = file.read()
#     print(content)
    

# Define a function to remove numbers from a string
def remove_numbers(text):
    return re.sub(r'\d+\.\d+,', '', text)


def split_first_column(text):
    match = re.match(r'(\S+)\s+(.*)', text)
    if match:
        return match.groups()  # Returns a tuple (first part, second part)
    return text, ''  # In case there is no match, return the original text and an empty string

def remove_duplicate_columns(parts):
    seen = set()
    new_parts = []
    for part in parts:
        if part not in seen:
            seen.add(part)
            new_parts.append(part)
    return new_parts

# input_file = "C:/Users/admin/Desktop/wenjia/unique_tax_count_bigger_than_1.txt"
# output_file = 'C:/Users/admin/Desktop/wenjia/processed_file.txt'
# output_file_template = 'C:/Users/admin/Desktop/wenjia/processed_file{}.txt'  # Template for output files with numbering



input_file = 'textmining_resutls/unique_tax_itis.txt'
output_file_template = 'processed_file_part{}.txt'  # Template for output files with numbering
final_output_file = 'final_merged_output.txt'  # Final merged output file

processed_rows = []
word_to_pmcs = defaultdict(list)

with open(input_file, 'r', encoding='utf-8') as f:
    total_lines = sum(1 for line in f)
    
# seperate the file to expediate    
chunk_size = total_lines // 10
chunk_count = 1



with open(input_file, 'r', encoding='utf-8') as infile:
    for i, line in enumerate(tqdm(infile, total=total_lines, desc="Processing lines")):
        # Split the line by '|'
        parts = line.split('|')
        
        first_part, second_part = split_first_column(parts[0])
        
        # Remove numbers after decimals in the other columns
        cleaned_parts = [remove_numbers(part) for part in parts[1:-1]]
        
        # Combine the split first column with the cleaned parts
        final_parts = [first_part, second_part] + cleaned_parts
        
        # Remove the duplicates
        unique_parts = remove_duplicate_columns(final_parts)
        
        
        # Append the processed row to the list
        processed_rows.append(unique_parts)
        
        for word in unique_parts[1:]:  # Start from the second element as the first is the ID
            if first_part not in word_to_pmcs[word]:
                word_to_pmcs[word].append(first_part)
        
        if (i + 1) % chunk_size == 0 or i + 1 == total_lines:
            output_file = output_file_template.format(chunk_count)
            with open(output_file, 'w', encoding='utf-8') as outfile:
                for word, pmcs in word_to_pmcs.items():
                    pmc_line = ','.join(pmcs)
                    outfile.write(f"{word},{pmc_line}\n")
            print(f"Saved progress to '{output_file}'.")
            chunk_count += 1
            word_to_pmcs.clear()        
        
        # grouped_data[second_part].append(first_part)

all_word_to_pmcs = defaultdict(set)  # Use a set to avoid duplicates

for part in range(1, chunk_count):
    output_file = output_file_template.format(part)
    with open(output_file, 'r', encoding='utf-8') as infile:
        for line in infile:
            word, *pmcs = line.strip().split(',')
            all_word_to_pmcs[word].update(pmcs)

# Write the final merged output
with open(final_output_file, 'w', encoding='utf-8') as outfile:
    for word, pmcs in all_word_to_pmcs.items():
        pmc_line = ','.join(sorted(pmcs))  # Sort PMCs for consistency
        outfile.write(f"{word},{pmc_line}\n")

print(f"Final merged data saved to '{final_output_file}'.")

# Optionally, remove the part files after merging
for part in range(1, chunk_count):
    output_file = output_file_template.format(part)
    os.remove(output_file)
    print(f"Removed temporary file '{output_file}'.")


# with open(output_file, 'w', encoding='utf-8') as outfile:
#     for row in processed_rows:
#         cleaned_line = ','.join(row)
#         outfile.write(cleaned_line + '\n')
        
# Convert the list of processed rows into a DataFrame
# df = pd.read_csv(output_file, sep=',', header=None)

# Convert the DataFrame to long format
# df_long = df.melt(id_vars=[0, 1], var_name='Column', value_name='Value')
