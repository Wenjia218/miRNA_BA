
import argparse
import os
from Bio import SeqIO


parser = argparse.ArgumentParser(
                    prog='create_mirsyn',
                    description='input datafiles',
                    epilog='Text at the bottom of help')

parser.add_argument('-mb', '--mirbase')      # option that takes a value
parser.add_argument('-mg', '--mirgenedb')
parser.add_argument('-p', '--pmiren')

args = parser.parse_args()
mirbase_path = args.mirbase
mirgenedb_path = args.mirgenedb
pmiren_path = args.pmiren

from Bio import SeqIO
from matplotlib_venn import venn3
import matplotlib.pyplot as plt

# Parse FASTA files and extract sequences
def get_unique_sequences(fasta_file):
    sequences = set()
    for record in SeqIO.parse(fasta_file, "fasta"):
        sequences.add(str(record.seq).replace('U', 'T'))  # Use sequence as unique identifier
    return sequences

# Files for three sources
source1 = args.mirbase
source2 = args.mirgenedb

# Get unique sequences from each source
seqs1 = get_unique_sequences(source1)
seqs2 = get_unique_sequences(source2)

import os
from Bio import SeqIO

# Function to extract sequences from multiple FASTA files in a folder
def get_sequences_from_folder(folder_path):
    sequences = set()
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".fa"):  # Check for FASTA files
            file_path = os.path.join(folder_path, file_name)
            for record in SeqIO.parse(file_path, "fasta"):
                sequences.add(str(record.seq).replace('U', 'T'))  # Use sequence as unique identifier
    return sequences

# Folder containing multiple FASTA files
folder_path = args.pmiren
seqs_from_folder = get_sequences_from_folder(folder_path)



# Calculate overlaps
unique1 = len(seqs1 - seqs2 - seqs_from_folder)
unique2 = len(seqs2 - seqs1 - seqs_from_folder)
unique_folder = len(seqs_from_folder - seqs1 - seqs2)
shared12 = len(seqs1 & seqs2 - seqs_from_folder)
shared13 = len(seqs1 & seqs_from_folder - seqs2)
shared23 = len(seqs2 & seqs_from_folder - seqs1)
shared123 = len(seqs1 & seqs2 & seqs_from_folder)


# Venn diagram for the three data sources
plt.figure(figsize=(8, 6))
venn3(subsets=(unique1, unique2, shared12, unique_folder, shared13, shared23, shared123),
      set_labels=('miRBase', 'MirGeneDB', 'PmiREN'))
plt.title("Overlap of miRNA Sequences Between Databases")
plt.show()

'''

from Bio import SeqIO
import os

def get_mirna_ids(fasta_file):
    """Extract miRNA IDs from a FASTA file."""
    mirna_ids = set()
    for record in SeqIO.parse(fasta_file, "fasta"):
        # Extract ID from the FASTA header (assumes '>'ID description format)
        mirna_id = record.id.split()[0]  # Take the first part of the header
        mirna_ids.add(mirna_id)
    return mirna_ids

def get_mirna_ids_from_folder(folder_path):
    """Extract miRNA IDs from all FASTA files in a folder."""
    mirna_ids = set()
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".fa"):  # Check for FASTA files
            file_path = os.path.join(folder_path, file_name)
            print(file_path)
            mirna_ids.update(get_mirna_ids(file_path))
    return mirna_ids

# Load miRNA IDs from different sources
mirna_ids1 = get_mirna_ids(args.mirbase)
mirna_ids2 = get_mirna_ids(args.mirgenedb)
mirna_ids_folder = get_mirna_ids_from_folder(args.pmiren)

# Compute overlaps
unique1 = len(mirna_ids1 - mirna_ids2 - mirna_ids_folder)
unique2 = len(mirna_ids2 - mirna_ids1 - mirna_ids_folder)
unique_folder = len(mirna_ids_folder - mirna_ids1 - mirna_ids2)
shared12 = len(mirna_ids1 & mirna_ids2 - mirna_ids_folder)
shared13 = len(mirna_ids1 & mirna_ids_folder - mirna_ids2)
shared23 = len(mirna_ids2 & mirna_ids_folder - mirna_ids1)
shared123 = len(mirna_ids1 & mirna_ids2 & mirna_ids_folder)

from matplotlib_venn import venn3
import matplotlib.pyplot as plt

# Plot Venn diagram
plt.figure(figsize=(8, 6))
venn3(subsets=(unique1, unique2, shared12, unique_folder, shared13, shared23, shared123),
      set_labels=('Source 1', 'Source 2', 'Folder'))
plt.title("Overlap of miRNA IDs Between Sources")
plt.show()
'''