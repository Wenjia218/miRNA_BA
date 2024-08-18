
id_counts = {}
PMC_counts = {}
with open('myresults/db.txt') as f:
    lines = f.readlines()
    for line in lines:
        if len(line.split(": ")) > 1:
            seq = line.split(": ")[0]
            real_line = line.split(": ")[1]
            ids = real_line.split(" | ")[0].split(", ")
            if len(real_line.split(" | ")) == 1:
                PMC_counts[seq] = 0
            else:
                PMCs = real_line.split(" | ")[1].split(", ")
                PMC_counts[seq] = len(PMCs)
            id_counts[seq] = len(ids)


def sort_dict_by_values(input_dict):
    sorted_items = sorted(input_dict.items(), key=lambda item: item[1], reverse=True)
    sorted_dict = dict(sorted_items)
    return sorted_dict

id_counts = sort_dict_by_values(id_counts)
PMC_counts = sort_dict_by_values(PMC_counts)

with open('myresults/db_counts.txt', 'w') as f:
    for line in id_counts:
        f.write(line)
        f.write(": " + str(id_counts[line]))
        f.write('\n')

with open('myresults/db_paper_counts.txt', 'w') as f:
    for line in PMC_counts:
        f.write(line)
        f.write(": " + str(PMC_counts[line]))
        f.write('\n')