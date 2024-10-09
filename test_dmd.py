mir_papers = {}
filename = 'syn/mirna_new_no3p5p.syn'
f = open(filename, encoding="utf-8")
lines = f.readlines()
for line in lines:
    list = line.split(": ")
    seq = list[0]
    line1 = list[1]
    mir_papers[seq] = line1

dmd = {}
filename = 'data/DMD/grape.txt'
f = open(filename, encoding="utf-8")
lines = f.readlines()
for line in lines:
    seq = line.split("	")[3].strip("\n")
    id = line.split("	")[1]
    dmd[id] = seq

for id in dmd:
    found_it = False
    for seq in mir_papers:

        if seq == dmd[id]:
            print("found it ")
            print(mir_papers[seq])
            found_it = True

    if found_it == False:
        print("unfound: " + id)
