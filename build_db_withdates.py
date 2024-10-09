
tax_PMCs = {}

with open('myresults/db_mir_FORM_bigger3_tax_in_ta') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip("\n")
        tax_PMCs[line.split(":")[0]] = line.split(":")[1]

tax_dates = {}

with open('myresults/FORM_bigger3_tax_in_ta_withdate.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip("\n")
        if line.split(" ")[1] != "1":
            tax_dates[line.split(" ")[0]] = line.split(" ")[1].strip("\n")

def sort_dict_by_values(input_dict):
    sorted_items = sorted(input_dict.items(), key=lambda item: item[1], reverse=False)
    sorted_dict = dict(sorted_items)
    return sorted_dict


output = {}
for organism in tax_PMCs:
    value_dic = {}
    for pmc in tax_PMCs[organism].split(","):
        if pmc in tax_dates:
            value_dic[pmc] = tax_dates[pmc]
        else:
            value_dic[pmc] = "/"
    output[organism] = sort_dict_by_values(value_dic)




def dict_to_string(d):
    str = ""
    for key in d:
        if str == "":
            str = key + ":" + d[key]
        else:
            str = str + ", " + key + ":" + d[key]
    return str

with open('myresults/db_mir_FORM_bigger3_tax_in_ta_withdates', 'w') as f:
    for organism in output:
        f.write(organism)
        f.write(": " + dict_to_string(output[organism]))
        f.write('\n')

