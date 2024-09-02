# Importing the csv module
import csv
# Opening the csv file in read mode
data = []
filename = "syn/ncbitaxon.syn"
f = open(filename, encoding="utf-8")
lines = f.readlines()
row_number = 1
output_line = ""
for line in lines:
    number = int(line.split("\t|\t")[0])
    if number == row_number:
        output_line = output_line + line
    else:
        output_line = output_line.replace("\t", "")
        output_line = output_line.replace("\n", "")
        data.append(output_line)
        output_line = line
        row_number = number

print(data)



with open('syn/ncbitaxon_plants.syn', 'w') as f:
    for line in syn_list:
        f.write(line)
        f.write('\n')


