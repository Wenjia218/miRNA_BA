FORM_counts = {}
FORM_positions = {}
PMC_lines = {}
with open('textmining_results/unique_tax_itis.txt', 'r', encoding="utf-8") as f:
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


with open('textmining_results/unique_tax_itis_count_bigger_than_3', 'w', encoding="utf-8") as f:
    for line in bigger_than_3:
        f.write(line)

topic_abstract = []
for PMC in FORM_counts:
    if FORM_positions[PMC] < 3:
        topic_abstract.append(PMC_lines[PMC])


with open('textmining_results/unique_tax_itis_in_topic_or_abstract', 'w', encoding="utf-8") as f:
    for line in topic_abstract:
        f.write(line)

topic = []
for PMC in FORM_counts:
    if FORM_positions[PMC] < 2:
        topic.append(PMC_lines[PMC])

topic_lines = []
for line in topic:
    line = line.split(" counts")[0]
    list = line.split(",")
    new_line = ""
    for item in list:
        if "1.1" in item:
            if new_line == "":
                new_line = item
            else:
                new_line = new_line + "," + item
    if new_line != "":
        topic_lines.append(new_line + "\n")

print(topic_lines)

with open('textmining_results/unique_tax_itis_in_topic', 'w', encoding="utf-8") as f:
    for line in topic_lines:
        f.write(line)

print("count of PMC in list of tax in topic: " + str(len(topic)))  # 220443
print("count of PMC in list of tax in topic or abstract: " + str(len(topic_abstract)))  # 474952
print("count of PMC in list of tax > 3: " + str(len(bigger_than_3)))  # 865994
print("count of all PMCs with synonym word: " + str(len(PMC_lines))) # 1836816