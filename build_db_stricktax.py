
file_lines = {}
filename = "myresults/db_alltax_itis.txt"
f = open(filename, encoding="utf-8")
lines = f.readlines()
for line in lines:
    taxname = line.split(",")[0]
    file_lines[taxname] = line


list_of_PMCs = []
#filename2 = "intersections/test.txt"
filename2 = "intersections/FORM_bigger3_tax_itis_in_topic_abstract.txt"
f = open(filename2, encoding="utf-8")
lines = f.readlines()
for line in lines:
    line = line.strip("\n")
    list_of_PMCs.append(line)


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

new_file_lines = {}

for tax in file_lines:
    list = file_lines[tax].split(",")
    list.pop(0)
    new_line = ""
    for item in list:
        if item in list_of_PMCs:
            if new_line == "":
                new_line = item
            else:
                new_line = new_line + "," + item
    tax = tax.lower()
    if new_line != "":
        if tax not in new_file_lines:
            new_file_lines[tax] = new_line
        else:
            new_file_lines[tax] = new_file_lines[tax] + "," + new_line
    print(tax + ": " + new_line)

output_lines = {}
for tax in new_file_lines:
    tax = tax.lower()
    if tax in synonyms and "PMC" in new_file_lines[tax]:
        tax_id = synonyms[tax]
        if tax_id not in output_lines:
            output_lines[tax_id] = new_file_lines[tax]
        else:
            output_lines[tax_id] = output_lines[tax_id] + "," + new_file_lines[tax]



with open('myresults/db_FORM_bigger3_tax_in_topic_abstract', 'w', encoding="utf-8") as f:
    for line in output_lines:
        f.write(line + ":" + output_lines[line] + "\n")
