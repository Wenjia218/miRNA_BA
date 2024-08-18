import glob

files = glob.glob("results/*.index")
plant_dic = {}
plant_count = {}
for file in files:
    with open(file, mode='r') as file:
        lines = file.readlines()
        for line in lines:
            list = line.split("	")
            PMC = list[0].split(".")[0]
            key_word = list[2]
            if PMC not in plant_dic:
                plant_dic[PMC] = key_word
            elif key_word not in plant_dic[PMC]:
                plant_dic[PMC] = plant_dic[PMC] + "," + key_word
            if PMC not in plant_count:
                plant_count[PMC] = 1
            else:
                plant_count[PMC] = plant_count[PMC] + 1

with open('unique_results/unique_results_withallwords.txt', 'w') as f:
    for PMC in plant_dic:
        f.write(PMC + " " + plant_dic[PMC] + " " + str(plant_count[PMC]))
        f.write('\n')


files2 = glob.glob("results2/*.index")
mirna_dic = {}
mirna_counts = {}
for file in files2:
    with open(file, mode='r') as file:
        lines = file.readlines()
        for line in lines:
            list = line.split("	")
            PMC = list[0].split(".")[0]
            key_word = list[2]
            if PMC not in mirna_dic:
                mirna_dic[PMC] = key_word
            elif key_word not in mirna_dic[PMC]:
                mirna_dic[PMC] = mirna_dic[PMC] + "," + key_word
            if PMC not in mirna_counts:
                mirna_counts[PMC] = 1
            else:
                mirna_counts[PMC] = mirna_counts[PMC] + 1

with open('unique_results/unique_results2_withallwords.txt', 'w') as f:
    for PMC in mirna_dic:
        f.write(PMC + " " + mirna_dic[PMC] + " " + str(mirna_counts[PMC]))
        f.write('\n')


files3 = glob.glob("results3/*.index")
FORM_dic = {}
FORM_counts = {}
for file in files3:
    with open(file, mode='r') as file:
        lines = file.readlines()
        for line in lines:
            list = line.split("	")
            PMC = list[0].split(".")[0]
            key_word = list[2]
            if PMC not in FORM_dic:
                FORM_dic[PMC] = key_word
            elif key_word not in FORM_dic[PMC]:
                FORM_dic[PMC] = FORM_dic[PMC] + "," + key_word
            if PMC not in FORM_counts:
                FORM_counts[PMC] = 1
            else:
                FORM_counts[PMC] = FORM_counts[PMC] + 1

with open('unique_results/unique_results3_withallwords.txt', 'w') as f:
    for PMC in FORM_dic:
        f.write(PMC + " " + FORM_dic[PMC] + " " + str(FORM_counts[PMC]))
        f.write('\n')
