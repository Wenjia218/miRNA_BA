'''

filename = "myresults/FORM_bigger3_tax_in_ta_withtitle.txt"
PMC_topic = {}
f = open(filename, encoding="utf-8")
lines = f.readlines()
for line in lines:
    PMC = line.split(" ")[0]
    new_list = line.split(" ")
    new_list.pop(0)
    title = ' '.join(new_list).strip("\n")
    PMC_topic[PMC] = title

keyword = ["sequence", "sequencing", "profiling", "discover", "identifying", "identification", "annotation", "prediction", "characterization",
           "Sequence", "Sequencing", "Profiling", "Discover", "Identifying", "Identification", "Annotation", "Prediction", "Characterization"]

output = {}

for item in PMC_topic:
    title = PMC_topic[item]
    title_list = title.split(" ")
    for word in keyword:
        if word in title_list:
            output[item] = title
            break
'''


filename = "textmining_results/unique_tax_itis_in_topic"
PMCs = []
f = open(filename, encoding="utf-8")
lines = f.readlines()
for line in lines:
    PMCs.append(line.split(" ")[0])

filename = "myresults/Sequencing_FORM_bigger3_tax_in_ta.txt"
PMC_topic = {}
f = open(filename, encoding="utf-8")
lines = f.readlines()
for line in lines:
    if line.split(" ")[0] in PMCs:
        PMC_topic[line.split(" ")[0]] = line


output_file = "myresults/Sequencing_FORM_bigger3_tax_in_topic.txt"
with open(output_file, mode='w', encoding="utf-8") as file:
    for line in PMC_topic:
        file.write(PMC_topic[line])




