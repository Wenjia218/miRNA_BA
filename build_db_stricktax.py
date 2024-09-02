
file_lines = {}
filename = "myresults/final_merged_output.txt"
f = open(filename, encoding="utf-8")
lines = f.readlines()
for line in lines:
    taxname = line.split(",")[0]
    file_lines[taxname] = line


list_of_PMCs = []
filename2 = "intersections/strick_mir_tax_papers.txt"
f = open(filename2, encoding="utf-8")
lines = f.readlines()
for line in lines:
    line = line.strip("\n")
    list_of_PMCs.append(line)

new_file_lines = {}
carrots = []

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
    new_file_lines[tax] = new_line


with open('myresults/db_strick_taxplant', 'w', encoding="utf-8") as f:
    for line in new_file_lines:
        f.write(line + ":" + new_file_lines[line] + "\n")
