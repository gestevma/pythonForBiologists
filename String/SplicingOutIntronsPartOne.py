#################################################################################
#Here's a short section of genomic DNA:
#ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT
#It comprises two exons and an intron. The first exon runs from the start of the 
#sequence to the sixty-third character, and the second exon runs from the ninety-first character to the end of the sequence. 
#Write a program that will print just the coding regions of the DNA sequence. 
#################################################################################


dna_seq = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

#We need to obtain the exon sequence, so I cut from the beginning to 63 nucleotide,
# and from nucleotide 93 to final
exon1 = dna_seq[:63]
exon2 = dna_seq[90:]

#To obtain the coding sequence I just combine the two exons sequences
coding_dna = exon1 + exon2

print(coding_dna)
