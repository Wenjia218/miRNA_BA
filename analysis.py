FORM_papers = {}
with open('textmining_resutls/unique_results3_withallwords.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.split("\n")[0]
        line = line.replace("small RNA", "small-RNA")
        line = line.replace("small RNAs", "small-RNAs")
        line = line.replace("Small RNA", "small-RNA")
        line = line.replace("Small RNAs", "small-RNAs")
        list = line.split(" ")
        PMC = list[0]
        count = list[2]
        if PMC not in FORM_papers:
            FORM_papers[PMC] = count

print(FORM_papers)