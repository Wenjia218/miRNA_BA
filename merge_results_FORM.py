import glob

files3 = glob.glob("results3/*.index")
FORM_dic = {}
FORM_counts = {}
FORM_positions = {}


for file in files3:
    with open(file, mode='r') as file:
        lines = file.readlines()
        for line in lines:
            list = line.split("	")
            PMC = list[0].split(".")[0]
            paragraph = list[0].split(".")[1]
            pos = list[0].split(".")[2]
            key_word = list[2]
            if PMC not in FORM_dic:
                FORM_dic[PMC] = key_word
                FORM_positions[PMC] = ""
                counts = 0
            elif key_word not in FORM_dic[PMC].split(","):
                FORM_dic[PMC] = FORM_dic[PMC] + "," + key_word

            position = str(paragraph) + "." + str(pos)
            if position not in FORM_positions[PMC].split(","):
                if FORM_positions[PMC] != "":
                    FORM_positions[PMC] = FORM_positions[PMC] + "," + position
                else:
                    FORM_positions[PMC] = position
                counts = counts + 1
            FORM_counts[PMC] = counts

with open('unique_results/unique_FORM_withallwords.txt', 'w') as f:
    for PMC in FORM_dic:
        f.write(PMC + " " + FORM_dic[PMC] + " counts: " + str(FORM_counts[PMC]) + " position: " + FORM_positions[PMC])
        f.write('\n')
