
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
        id = line.split(": ")[0]
        seq = line.split(": ")[1]
        motifs3[seq] = id

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

for seq in motifs_all:
    list_of_mirnas = []
    ids = motifs_all[seq]
    list_of_ids = ids.split(", ")
    for id in list_of_ids:
        list = id.split(" ")
        list_of_words = list[0].split("-")
        if len(list_of_words) >= 3:
            mir_id = list_of_words[1] + "-" + list_of_words[2]
        else:
            mir_id = list_of_words[1]
        if mir_id not in list_of_mirnas:
            list_of_mirnas.append(mir_id)

print(len(motifs))
print(len(motifs2))
print(len(motifs3))
print(len(motifs_all))

with open('myresults/db_noPMC.txt', 'w') as f:
    for line in motifs_all:
        f.write(line)
        f.write(": " + motifs_all[line])
        f.write('\n')



mirnas = []
for item in motifs_all:
    list_of_ids = []
    for ids in motifs_all[item].split(", "):
        for id in ids.split(" "):
            if id not in list_of_ids:
                list_of_ids.append(id)
    line_of_ids = ""
    for id_in_list in list_of_ids:
        line_of_ids = line_of_ids + "|" + id_in_list
    line = item + ": " + item  + "|" + item.replace("U", "T") + line_of_ids
    mirnas.append(line)

with open('syn/mirna_new.syn', 'w') as f:
    for line in mirnas:
        f.write(line)
        f.write('\n')
