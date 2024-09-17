FORM_counts = {}
FORM_positions = {}
PMC_lines = {}
with open('textmining_results/unique_FORM_withallwords.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        PMC = line.split(" ")[0]
        PMC_lines[PMC] = line
        count = int(line.split("counts: ")[1])
        position = int(line.split("|")[1].split(",")[0][0])
        if PMC not in FORM_counts:
            FORM_counts[PMC] = count
        if PMC not in FORM_positions:
            FORM_positions[PMC] = position

bigger_than_3 = []
for PMC in FORM_counts:
    if FORM_counts[PMC] > 3:
        bigger_than_3.append(PMC_lines[PMC])


with open('textmining_results/unique_FORM_count_bigger_than_3', 'w') as f:
    for line in bigger_than_3:
        f.write(line)

topic_abstract = []
for PMC in FORM_counts:
    if FORM_positions[PMC] < 3:
        topic_abstract.append(PMC_lines[PMC])


with open('textmining_results/unique_FORM_in_topic_or_abstract', 'w') as f:
    for line in topic_abstract:
        f.write(line)