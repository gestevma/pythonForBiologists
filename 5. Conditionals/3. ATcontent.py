#######################################################################################
# From data.csv
# Print out the gene names for all genes whose AT content is less than 0.5 and whose
# expression level is greater than 200.
#######################################################################################

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
    gene_expresion = int(gene_atributes[3])
    
    #Obtain the AT content
    at_quantity = gene_sequence.upper().count("A") + gene_sequence.upper().count("T")
    at_content = at_quantity/len(gene_sequence)
    
    #Print gene names from genes with less AT content than 0.5 and a gene expression greather than 200
    if at_content < 0.5 and gene_expresion > 200:
        print(gene_name)