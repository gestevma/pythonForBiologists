########################################################################
# From data.csv
# Print out the gene names for all genes between 90 and 110 bases long.
########################################################################

#Order of columns in data.csv:
    # 0-->specie
    # 1-->gene_sequence
    # 2-->gene_name
    # 3-->expresion_level
    
genes_file = open("data.csv")

for gene in genes_file:
    
    gene_atributes = gene.split(",")
    
    gene_sequence = gene_atributes[1]
    gene_name = gene_atributes[2]
    
    #Obtain the gene names from genes between 90 and 110 bases long
    if len(gene_sequence) >= 90 and len(gene_sequence) <= 110:
        print(gene_name)
        