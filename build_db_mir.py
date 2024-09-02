
motifs = {}

with open('data/mature.fa') as f:
    lines = f.readlines()
    for i in range(0, len(lines)):
        s = lines[i].strip('\n')
        if s[0] == '>':
            str = s[1:]
            list = str.split(" ")
            ids = list[0] + " " + list[1] + " " + list[4]
        else:
            if s not in motifs:
                motifs[s] = ids
            else:
                motifs[s] = motifs[s] + ", " + ids

motifs2 = {}

with open('data/ALL.fas') as f:
    lines = f.readlines()
    for i in range(0, len(lines)):
        s = lines[i].strip('\n')
        if s[0] == '>':
            str = s[1:]
            ids = str
        else:
            if s not in motifs2:
                motifs2[s] = ids
            else:
                motifs2[s] = motifs2[s] + ", " + ids



motifs3 = {}

with open('data/all_plant_mirnas.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip("\n")
        seq = line.split(": ")[0]
        id = line.split(": ")[1]
        if seq not in motifs3:
            motifs3[seq] = id
        else:
            motifs3[seq] = motifs3[seq] + ", " + id


list_of_sequences = []
for key in motifs:
    list_of_sequences.append(key)

for key in motifs2:
    if key not in list_of_sequences:
        list_of_sequences.append(key)

for key in motifs3:
    if key not in list_of_sequences:
        list_of_sequences.append(key)


motifs_all = {}
for seq in list_of_sequences:
    if seq in motifs:
        if seq in motifs_all:
            motifs_all[seq] = motifs_all[seq] + ", " + motifs[seq]
        else:
            motifs_all[seq] = motifs[seq]
    if seq in motifs2:
        if seq in motifs_all:
            motifs_all[seq] = motifs_all[seq] + ", " + motifs2[seq]
        else:
            motifs_all[seq] = motifs2[seq]
    if seq in motifs3:
        if seq in motifs_all:
            motifs_all[seq] = motifs_all[seq] + ", " + motifs3[seq]
        else:
            motifs_all[seq] = motifs3[seq]
    motifs_all[seq] = motifs_all[seq] + " | "


# add PMC to the database
PMC_dic = {}
with open('textmining_resutls/unique_results2_withallwords.txt') as f:
    lines = f.readlines()
    for line in lines:
        list = line.split(" ")
        PMC = list[0]
        if PMC not in PMC_dic:
            PMC_dic[PMC] = list[1]


for seq in motifs_all:
    list_of_mirnas = []
    ids = motifs_all[seq]
    list_of_ids = ids.split(", ")
    for id in list_of_ids:
        list = id.split(" ")
        if len(list) == 1:
            mir_id = list[0]
        else:
            mir_id = list[2]
        if mir_id not in list_of_mirnas:
            list_of_mirnas.append(mir_id)
    for pmc in PMC_dic:
        for mir in list_of_mirnas:
            if mir in PMC_dic[pmc].split(","):
                if "PMC" not in motifs_all[seq]:
                    motifs_all[seq] = motifs_all[seq] + pmc
                else:
                    motifs_all[seq] = motifs_all[seq] + ", " + pmc
                break


with open('myresults/db.txt', 'w') as f:
    for line in motifs_all:
        f.write(line)
        f.write(": " + motifs_all[line])
        f.write('\n')
