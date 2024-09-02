
tax_syn = {}
filename = "syn/ncbitaxon.33090.syn"
f = open(filename, encoding="utf-8")
lines = f.readlines()
for line in lines:
    if len(line.split("|")) > 1:
        sci_name = line.split("|")[1]
        tax_syn[sci_name] = line.strip("\n")

itis = {}
filename = "myresults/itis.txt"
f = open(filename, encoding="utf-8")
lines = f.readlines()
for line in lines:
    itis[line.split(": ")[0]] = line.split(": ")[1].strip("\n")


write_lines = []

for key in tax_syn:
    if key in itis:
        itis_syn = itis[key].replace(", ", "|")
        write_lines.append(tax_syn[key] + "|" + itis_syn)
    else:
        write_lines.append(tax_syn[key])

print(len(write_lines))

with open('syn/ncbitaxon.33090_itis.syn', 'w', encoding="utf-8") as f:
    for line in write_lines:
        f.write(line)
        f.write('\n')


