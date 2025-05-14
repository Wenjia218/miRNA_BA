# Analysis of plant miRNAs with text mining
This is the repository for the bachelor thesis of Wenjia Zhong. Text mining methods were used to extract valuable data from publications.
The project is mainly down by python, some of the plots were done using R and ITOL. 




# Pipeline of text mining and visualization of results
create_mirsyn.py    create synonym list of miRNAs names and sequences from the miRNA databases
#python3 create_mirsyn.py -mb 'data/mature.fa' -mg 'data/ALL.fas' -p 'data/all_plant_mirnas.txt'
#the synonym list is called no3p5p, because each miRNA name without suffix is added in order to capture all possible miRNA names in textmining

create_taxsyn.py    create synonym list of plant names and NCBI tax ID using the NCBI taxonomy list: ncbitaxon.33090.syn and the ITIS list: itis.txt
#python3 create_taxsyn.py -n Synfile/ncbitaxon.33090.syn -i myresults/itis.txt
#the synonym list is called new because some plant names have been deleted from the list due to their ambiguous meaning

textmineDocument.py     the textmining tool from Dr. rer. nat.MarkusJoppich, that takes in a synonym list and the data of PMC or pubmed publications
#the tool is able to take in multiple synonym files at one time, however, each synonym list was taken seperately, which caused a very long processing time but easier for dealing with the results
#python3 textmineDocument.py --threads 14 --synonyms Synfile/mirna_new_no3p5p.syn --output ./pubmed_results_mir_no3p5p --input /mnt/extproj/projekte/textmining/pubmed_feb24/*.sent
#python3 textmineDocument.py --threads 14 --synonyms Synfile/ncbitaxon.33090_itis_new.syn --output ./pubmed_results_tax_new --input /mnt/extproj/projekte/textmining/pubmed_feb24/*.sent
#python3 textmineDocument.py --threads 14 --synonyms Synfile/FORM.syn --output ./pubmed_results_FORM --input /mnt/extproj/projekte/textmining/pubmed_feb24/*.sent
#python3 textmineDocument.py --threads 14 --synonyms Synfile/FORM.syn --output ./results_FORM --input /mnt/raidexttmp/pmc_sep24/oa_bulk/oa_comm/xml/*.sent
#python3 textmineDocument.py --threads 14 --synonyms Synfile/mirna_new_no3p5p.syn --output ./results_mir_no3p5p --input /mnt/raidexttmp/pmc_sep24/oa_bulk/oa_comm/xml/*.sent
#python3 textmineDocument.py --threads 14 --synonyms Synfile/ncbitaxon.33090_itis_new.syn --output ./results_tax_itis_new --input /mnt/raidexttmp/pmc_sep24/oa_bulk/oa_comm/xml/*.sent

merge_results.py    merge the text mining results of many seperate result files in a folder where each line of one found synonym word in text to one file of all results where each line is one paper and all six results are stored in the textmining_results folder
#python3 merge_results.py --input "results_mir_no3p5p/" --output "textmining_results/PMC_mir" 
#python3 merge_results.py --input "results_tax_itis/" --output "textmining_results/PMC_tax" 
#python3 merge_results.py --input "results_FORM/" --output "textmining_results/PMC_FORM" 
#python3 merge_results.py --input "pubmed_results_FORM/" --output "textmining_results/pubmed_FORM"
#python3 merge_results.py --input "pubmed_results_mir_no3p5p/" --output "textmining_results/pubmed_mir"
#python3 merge_results.py --input "pubmed_results_tax_itis/" --output "textmining_results/pubmed_tax_itis"

calculated_scores.py calculate scores of each synonym for their frequencies, positions in text and so on

build_dataframe_alltextmining.py    store all three textmining results: tax, mir and FORM in a pandas dataframe and output in a csv file with the calculated scores, PubMed and PMC are stored seperately
#python build_dataframe_alltextmining.py -t "textmining_results/PMC_tax_withallwords" -f "textmining_results/PMC_FORM_withallwords" -m "textmining_results/PMC_mir_withallwords"
#python build_dataframe_alltextmining.py -t "textmining_results/pubmed_tax_withallwords" -f "textmining_results/pubmed_FORM_withallwords" -m "textmining_results/pubmed_mir_withallwords"

intersect.py 
intersect_pubmed.py create intersection of textmining results which represents possible relevant papers of plant miRNAs
#python intersect.py --input "myresults/dataframe_alltextmining.csv"
#python intersect_pubmed.py --input "myresults/pubmed_dataframe_alltextmining.csv"

dataframe.select.py     select rows from the dataframe of a given list of PMC or PubMed ID

get_data_and_title.py   get the publish date and titles of a list of papers from the PMC/PubMed data on the server

get_pubid.py    get the PubMed ID of a list of given PMC id from the PMC/PubMed data

get_title_Seqeuncing.py     get the papers with possible sequencing data from a list of papers with their titles

ITOL_xxxx.py    scripts that output data or tree file for ITOL plots (Figure 3.17 & 3.18)

make_phylogenie_ggtree.R    the R script that create phylogenetic tree of a given list of species, thanks to Bui!

print_timeline.py   the script that create a time line plot of a list of papers on one plant or miRNA, ordered with their dates, can be created for certain groups of papers such as papers with sequencing data or papers that mentioned the plant or miRNA or focus on the plant or miRNA
#python print_timeline.py -t tax -i carrot -s
#python print_timeline.py -t mir -i mir-156 -it

plot_cloud.py   print a cloud plot for a given PMC ID which is in the dataframe

# in plotting/
plot_bekannt_vs_textmining.py   plot the barplot with the comparison of plants and miRNAs that were known from databases and mentioned in publications

plot_benchmarking.py    plot the benchmarking results of TPs, FPs, TNs and FNs

plot_dates.py   plot the barplot of publication counts over the years

plot_miRNA.py   plot the counts of miRNAs of different plants based on miRNA DBs

plot_overlap_mirna_dbs.py   plot the miRNAs overlapped by same sequences from three miRNA DBs
