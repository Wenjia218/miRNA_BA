import glob

files2 = glob.glob("results_mir/*.index")
mirna_dic = {}
mirna_counts = {}
mirna_position = {}

for file in files2:
    with open(file, mode='r') as file:
        lines = file.readlines()
        for line in lines:
            list = line.split("	")
            PMC = list[0].split(".")[0]
            paragraph = list[0].split(".")[1]
            pos = list[0].split(".")[2]
            key_word = list[2]
            if PMC not in mirna_dic:
                mirna_dic[PMC] = key_word
                mirna_position[PMC] = ""
                counts = 0
            elif key_word not in mirna_dic[PMC].split(","):
                mirna_dic[PMC] = mirna_dic[PMC] + "," + key_word

            position = str(paragraph) + "." + str(pos)
            if position not in mirna_position[PMC].split(","):
                if mirna_position[PMC] != "":
                    mirna_position[PMC] = mirna_position[PMC] + "," + position
                else:
                    mirna_position[PMC] = position
                counts = counts + 1
            mirna_counts[PMC] = counts

with open('unique_results/unique_mir_withallwords.txt', 'w') as f:
    for PMC in mirna_dic:
        f.write(PMC + " " + mirna_dic[PMC] + " counts: " + str(mirna_counts[PMC]) + " position: " + mirna_position[PMC])
        f.write('\n')