#################################################################################
# Here's a short DNA sequence:
# ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT
# Write a program that will print out the AT content of this DNA sequence.
#################################################################################


dna_seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

#AT content: percentaje of A+T in the sequence
#formula ((A+T)/len(dna_seq))*100

count_A = dna_seq.count("A")
count_T =dna_seq.count("T")
dna_len = len(dna_seq)

percentaje_AT = ((count_A+count_T)/dna_len)*100

print("percentaje AT: " + str(percentaje_AT) + "%")