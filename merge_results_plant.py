import glob

files = glob.glob("results/*.index")
plant_dic = {}
plant_counts = {}
plant_position = {}

for file in files:
    with open(file, mode='r') as file:
        lines = file.readlines()
        for line in lines:
            list = line.split("	")
            PMC = list[0].split(".")[0]
            paragraph = list[0].split(".")[1]
            pos = list[0].split(".")[2]
            key_word = list[2]
            if PMC not in plant_dic:
                plant_dic[PMC] = key_word
                plant_position[PMC] = ""
                counts = 0
            elif key_word not in plant_dic[PMC].split(","):
                plant_dic[PMC] = plant_dic[PMC] + "," + key_word

            position = str(paragraph) + "." + str(pos)
            if position not in plant_position[PMC].split(","):
                if plant_position[PMC] != "":
                    plant_position[PMC] = plant_position[PMC] + "," + position
                else:
                    plant_position[PMC] = position
                counts = counts + 1
            plant_counts[PMC] = counts

with open('unique_results/unique_plant_withallwords.txt', 'w') as f:
    for PMC in plant_dic:
        f.write(PMC + " " + plant_dic[PMC] + " counts: " + str(plant_counts[PMC]) + " position: " + plant_position[PMC])
        f.write('\n')


