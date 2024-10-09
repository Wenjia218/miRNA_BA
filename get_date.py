import glob

file_list = "intersections/FORM_bigger3_tax_itis_in_topic_abstract.txt"
PMC_list = []
with open(file_list, mode='r') as file:
    lines = file.readlines()
    for line in lines:
        PMC_list.append(line.strip("\n"))


files3 = glob.glob("*.date")
output = {}

for file in files3:
    with open(file, mode='r', encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            PMC = line.split("	")[0]
            year = line.split("	")[1]
            for PMC_item in PMC_list:
                if PMC_item == PMC:
                    output[PMC] = year
                    PMC_list.remove(PMC_item)


output_file = "myresults/FORM_bigger3_tax_in_ta_withdate.txt"
with open(output_file, mode='w') as file:
    for line in output:
        file.write(line + " " + output[line])
        file.write('\n')
