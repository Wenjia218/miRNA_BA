import glob

files = glob.glob("results_taxonomy/*.index")
plant_dic = {}
plant_counts = {}

for file in files:
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

            if PMC not in plant_dic:
                plant_dic[PMC] = w_line
                counts = 1
            elif w_line not in plant_dic[PMC].split(","):
                plant_dic[PMC] = plant_dic[PMC] + "," + w_line
                counts = counts + 1

            plant_counts[PMC] = counts

with open('textmining_results/unique_tax_withallwords.txt', 'w') as f:
    for PMC in plant_dic:
        f.write(PMC + " " + plant_dic[PMC] + " counts: " + str(plant_counts[PMC]))
        f.write('\n')


