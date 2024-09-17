import glob

files2 = glob.glob("results_mir/*.index")
mirna_dic = {}
mirna_counts = {}

for file in files2:
    with open(file, mode='r') as file:
        lines = file.readlines()
        for line in lines:
            list = line.split("	")
            PMC = list[0].split(".")[0]
            paragraph = list[0].split(".")[1]
            pos = list[0].split(".")[2]
            position = str(paragraph) + "." + str(pos)
            key_word = list[2]

            w_line = key_word + "|" + position

            if PMC not in mirna_dic:
                mirna_dic[PMC] = w_line
                counts = 1
            elif w_line not in mirna_dic[PMC].split(","):
                mirna_dic[PMC] = mirna_dic[PMC] + "," + w_line
                counts = counts + 1

            mirna_counts[PMC] = counts

with open('textmining_results/unique_mir_withallwords.txt', 'w') as f:
    for PMC in mirna_dic:
        f.write(PMC + " " + mirna_dic[PMC] + " counts: " + str(mirna_counts[PMC]))
        f.write('\n')