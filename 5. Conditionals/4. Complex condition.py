###################################################################################
# From data.csv
# Print out the gene names for all genes whose name begins with "k" or "h" except
# those belonging to Drosophila melanogaster.
##################################################################################

#Order of columns in data.csv:
    # 0-->specie
    # 1-->gene_sequence
    # 2-->gene_name
    # 3-->expresion_level
    
genes_file = open("data.csv")

for gene in genes_file:
    gene_atributes = gene.split(",")
    
    gene_specie = gene_atributes[0]
    gene_name = gene_atributes[2]
    
    #Obtain gene_names from non droophila melanogaster and wich name starts with k or h
    if (gene_specie.lower() != "drosophila melanogaster" and (gene_name[0].lower() == "k" or gene_name[0].lower() == "h")):
        print(gene_name)