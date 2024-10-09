
db_mir = {}

with open('myresults/db_allmir.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip("\n")
        mir = line.split(",")[0]
        list = line.split(",")
        list.pop(0)
        mir = mir.lower()
        if mir not in db_mir:
            db_mir[mir] = ",".join(list)
        else:
            db_mir[mir] = db_mir[mir] + "," + ",".join(list)



list_of_PMCs = []
#filename2 = "intersections/test.txt"
filename2 = "intersections/FORM_bigger3_tax_itis_in_topic_abstract.txt"
f = open(filename2, encoding="utf-8")
lines = f.readlines()
for line in lines:
    line = line.strip("\n")
    list_of_PMCs.append(line)


output_lines = {}
for mir in db_mir:
    new_line = ""
    PMCs = db_mir[mir]
    PMCs_list = PMCs.split(",")
    for PMC in PMCs_list:
        if PMC in list_of_PMCs:
            if new_line == "":
                new_line = PMC
            else:
                new_line = new_line + "," + PMC
    print(new_line)
    if new_line != "":
        output_lines[mir] = new_line



with open('myresults/db_mir_FORM_bigger3_tax_in_ta', 'w', encoding="utf-8") as f:
    for line in output_lines:
        f.write(line + ":" + output_lines[line] + "\n")



