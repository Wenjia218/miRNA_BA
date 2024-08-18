import glob

files = glob.glob("data/plant_mirna/*.fa")
mirna = {}

for file in files:
    with open(file, mode='r') as file:
        lines = file.readlines()
        for i in range(0, len(lines)):
            s = lines[i].strip('\n')
            if s[0] == '>':
                id = s[1:]
            else:
                mirna[id] = s

with open('data/all_plant_mirnas.txt', 'w') as f:
    for line in mirna:
        f.write(line)
        f.write(": " + mirna[line])
        f.write('\n')