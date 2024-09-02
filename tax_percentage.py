
'''
# for producing the file without position and counts
filename = "textmining_resutls/filtered_mirtax_in_titel_abstract.txt"
unique_tax = {}
f = open(filename, encoding="utf-8")
lines = f.readlines()
for line in lines:
    PMC = line.split(" ")[0]
    taxs = []
    lists_of_words = line.split(" ")
    lists_of_words.pop(0)
    lists_of_words.pop(len(lists_of_words) - 1)
    lists_of_words.pop(len(lists_of_words) - 1)
    tax_string = ''.join(lists_of_words)
    for item in tax_string.split(","):
        taxs.append(item.split("|")[0] + ",")
    unique_tax[PMC] = ''.join(taxs)[:-1]

with open('textmining_resutls/filtered_tax_noCount.txt', 'w', encoding="utf-8") as f:
    for PMC in unique_tax:
        f.write(PMC + ": " + unique_tax[PMC] + "\n")

'''


def dic_to_line(dic):
    str_dic = ""
    for key in dic:
        str_dic = str_dic + key + ": " + dic[key] + ","
    return str_dic


percentages_of_paper = {}
filename = "textmining_resutls/filtered_tax_noCount.txt"
f = open(filename, encoding="utf-8")
lines = f.readlines()
for line in lines:
    line = line.strip("\n")
    PMC = line.split(": ")[0]
    list_of_syns = line.split(": ")[1].split(",")
    counts = {}
    percentages = {}
    sum_counts = 0
    for word in list_of_syns:
        if word != "":
            if (word[0].islower()):
                word = word.capitalize()
        if word not in counts:
            counts[word] = 1
            sum_counts = sum_counts + 1
        else:
            counts[word] = counts[word] + 1
            sum_counts = sum_counts + 1
    for item in counts:
        percentages[item] = str(round(counts[item] / sum_counts, 4))

    print(percentages)

    str_percentages = dic_to_line(percentages)
    percentages_of_paper[PMC] = str_percentages


with open('textmining_resutls/filtered_tax_percentage.txt', 'w', encoding="utf-8") as f:
    for PMC in percentages_of_paper:
        f.write(PMC + ": " + percentages_of_paper[PMC] + "\n")
