#################################################################################
#Here's a short section of genomic DNA:
#ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT
#It comprises two exons and an intron. The first exon runs from the start of the 
#sequence to the sixty-third character, and the second exon runs from the ninety-first character to the end of the sequence. 
#################################################################################

dna_seq = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"


#-------Part one-------#: 
# Write a program that will print just the coding regions of the DNA sequence.
#----------------------#

#We need to obtain the exon sequence, so I cut from the beginning to 63 nucleotide,
# and from nucleotide 93 to final
exon1 = dna_seq[:63]
exon2 = dna_seq[90:]

#To obtain the coding sequence I just combine the two exons sequences
coding_dna = exon1 + exon2

print("coding DNA: " + coding_dna)



#-------Part two:-------#
# Using the data from part one, 
# write a program that will calculate what percentage of the DNA sequence is coding.
#-----------------------#

#To calculate the percentatge of coding DNA we should calculate the length of coding DNA and total DNA
#(len(coding_dna)/len(dna_seq))*100

coding_percentage = (len(coding_dna)/len(dna_seq))*100

print("percentage of coding DNA: " + str(coding_percentage) + "%")



#-------Part three-------#
#Using the data from part one, write a program that will print out the original
#genomic DNA sequence with coding bases in uppercase and non-coding bases in
#lowercase.
#------------------------#

#For doing that I replace the exons for the same sequence in lowerCase

dna_seq_lower_introns = dna_seq

intron = dna_seq[63:90]

dna_seq_lower_introns = dna_seq_lower_introns.replace(intron, intron.lower())

print(dna_seq_lower_introns)