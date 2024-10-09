

tax_papers_and_dates = {}
with open('myresults/db_FORM_bigger3_tax_ta_withdates', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        tax_papers_and_dates[line.split(": ")[0]] = line.split(": ")[1].strip("\n")

mir_papers_and_dates = {}
with open('myresults/db_mir_FORM_bigger3_tax_in_ta_withdates', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        mir_papers_and_dates[line.split(": ")[0]] = line.split(": ")[1].strip("\n")

synonyms = {}  # key: each synonyms  value: the object that they belong to
filename3 = "syn/ncbitaxon.33090_itis.syn"
f = open(filename3, encoding="utf-8")
lines = f.readlines()
for line in lines:
    key = line.split(":")[0]
    words = line.split(":")[1].strip("\n").split("|")
    for word in words:
        word = word.lower()
        synonyms[word] = key

PMC_titles = {}
with open('myresults/FORM_bigger3_tax_in_ta_withtitle.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        list = line.split(" ")
        list.pop(0)
        PMC_titles[line.split(" ")[0]] = " ".join(list)

list_inputs = []

tax_or_mir = True
print('tax or miRNA?:')
type = input()
if type == "miRNA":
    tax_or_mir = False

if tax_or_mir:
    print('Enter taxonomy name:')
    tax = input()
    if tax in synonyms:
        list_inputs.append(tax)
    else:
        print("invalid input")
else:
    print('Enter miRNA name(lower case, with "-"):')
    miR = input()
    if miR in mir_papers_and_dates:
        list_inputs.append(miR)
    else:
        print("invalid input")

list_of_IDs = []
if tax_or_mir:
    for input_tax in list_inputs:
        ID = synonyms[input_tax]
        if ID not in list_of_IDs:
            list_of_IDs.append(ID)
else:
    for input_mir in list_inputs:
        list_of_IDs.append(input_mir)


output_lines = {}
for ID in list_of_IDs:
    if tax_or_mir:
        line_dates = tax_papers_and_dates[ID]
    else:
        line_dates = mir_papers_and_dates[ID]
    dict_dates = {}
    for item in line_dates.split(", "):
        if item.split(":")[1] != "/":
            dict_dates[item.split(":")[0]] = item.split(":")[1]

    dict_dates_topic = {}
    for PMC in dict_dates:
        title = PMC_titles[PMC]
        dict_dates_topic[PMC] = dict_dates[PMC] + "," + title.strip("\n")

    output_lines[ID] = dict_dates_topic

output_file = "myresults/timeline_output.txt"
with open(output_file, mode='w', encoding="utf-8") as file:
    for ID in output_lines:
        file.write(ID + ":" + "\n")
        for PMC in output_lines[ID]:
            file.write(PMC + ": " + output_lines[ID][PMC])
            file.write("\n")
            file.write("------>")
            file.write("\n")
