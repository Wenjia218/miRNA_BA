plantae_tax_id = 3193
taxa_under_plantae = []

with open('data/nodes.dmp', 'r') as nodes_file:
    for line in nodes_file:
        fields = line.strip().split('|')
        tax_id = int(fields[0].strip())
        parent_tax_id = int(fields[1].strip())

        # If the parent_tax_id is Plantae, it's a child taxon
        if parent_tax_id == plantae_tax_id:
            taxa_under_plantae.append(tax_id)

# Iterate to find all descendants
all_descendants = set(taxa_under_plantae)
while taxa_under_plantae:
    current_id = taxa_under_plantae.pop()
    with open('data/nodes.dmp', 'r') as nodes_file:
        for line in nodes_file:
            fields = line.strip().split('|')
            tax_id = int(fields[0].strip())
            parent_tax_id = int(fields[1].strip())

            if parent_tax_id == current_id:
                if tax_id not in all_descendants:
                    all_descendants.add(tax_id)
                    taxa_under_plantae.append(tax_id)

print(f"Total taxa under Plantae: {len(all_descendants)}")
