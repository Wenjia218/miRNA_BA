
scientific_names = []

with open('syn/ncbitaxon.33090.syn') as f:
    lines = f.readlines()
    for line in lines:
        if len(line.split("|")) > 1:
            name = line.split("|")[1]
            if '<' not in name:
                scientific_names.append(name)

with open('myresults/all_scientific_names.txt', 'w') as f:
    for line in scientific_names:
        f.write(line.strip("\n"))
        f.write('\n')