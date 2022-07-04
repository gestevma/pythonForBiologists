# For each gene, print out a message giving the gene name and saying whether its AT 
# content is high (greater than 0.65), low (less than 0.45) or medium (between 0.45 
# and 0.65).

#Order of columns in data.csv:
    # 0-->specie
    # 1-->gene_sequence
    # 2-->gene_name
    # 3-->expresion_level
    
file_genes = open("data.csv")

for gene in file_genes:
    gene_attributes = gene.split(",")

    gene_dna = gene_attributes[1].upper()
    gene_name = gene_attributes[2]

    #Obtain AT content
    AT_quantity = gene_dna.count("A") + gene_dna.count("T")
    AT_content = AT_quantity/len(gene_dna)

    #Indicate if the gene has a high, low or medium AT content
    if AT_content > 0.65:
        print(gene_name + " has a High AT content")
    elif AT_content < 0.45:
        print(gene_name + " has a Low AT content")
    else:
        print(gene_name + " has a Medium AT content") 