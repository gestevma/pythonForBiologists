#################################################################################
# Here's a short DNA sequence:
# ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT
# Write a program that will print the complement of this sequence
#################################################################################


dna_seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
dna_compl = dna_seq

#I can't replace the nucleotides directly because the program replace letter by letter, not at the same time.
#That means that if for example in sequence AGCTA i replace A by T (result TGCTA) and later T by A (result AGCAA) re result will be wrong
#To avoid that I need at least an auxiliar for each couple of nucleotides

dna_compl = dna_compl.replace("A", "S") #A auxiliar
dna_compl = dna_compl.replace("C", "R") #C auxiliar

dna_compl =  dna_compl.replace("T", "A")
dna_compl = dna_compl.replace("G", "C")
dna_compl = dna_compl.replace("S", "T")
dna_compl = dna_compl.replace("R", "G")

#Print master and complementari sequence
print("master-->" + dna_seq)
print("comple-->" + dna_compl)
