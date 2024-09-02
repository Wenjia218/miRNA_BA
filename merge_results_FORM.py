import glob

files3 = glob.glob("results3/*.index")
FORM_dic = {}
FORM_counts = {}


for file in files3:
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

            if PMC not in FORM_dic:
                FORM_dic[PMC] = w_line
                counts = 1
            elif w_line not in FORM_dic[PMC].split(","):
                FORM_dic[PMC] = FORM_dic[PMC] + "," + w_line
                counts = counts + 1

            FORM_counts[PMC] = counts

with open('unique_results/unique_FORM_withallwords.txt', 'w') as f:
    for PMC in FORM_dic:
        f.write(PMC + " " + FORM_dic[PMC] + " counts: " + str(FORM_counts[PMC]))
        f.write('\n')
