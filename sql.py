import csv

sci_tri = {}

with open('syn/sql.txt', encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
        list = line.split(", ")

        sci_name = list[len(list) - 7].strip("'").strip('"')
        tri_name = list[len(list) - 5].strip("'").strip('"')
        print(tri_name)

        if sci_name not in sci_tri:
            sci_tri[sci_name] = tri_name
        else:
            sci_tri[sci_name] = sci_tri[sci_name] + ", " + tri_name


with open('myresults/itis.txt', 'w') as f:
    for key in sci_tri:
        f.write(key + ": " + sci_tri[key])
        f.write('\n')