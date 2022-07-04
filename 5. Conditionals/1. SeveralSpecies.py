##################################################################################
# From data.csv
# Print out the gene names for all genes belonging to Drosophila melanogaster or
# Drosophila simulans.
##################################################################################

#Order of columns in data.csv:
    # 0-->specie
    # 1-->gene_sequence
    # 2-->gene_name
    # 3-->expresion_level
    
genes_file = open("data.csv")

for gene in genes_file:
    gene_atributes = gene.split(",")
    
    specie = gene_atributes[0]
    gene_name = gene_atributes[2]
    
    #Obtain the gene names if specie is drosophila melanogaster or drosophila simulans
    if specie.lower() == "drosophila melanogaster" or specie.lower() == "drosophila simulans":
        print(gene_name)

    