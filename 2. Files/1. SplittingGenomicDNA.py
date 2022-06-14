##############################################################################################
#Look for a file called genomic_dna.txt. Write a program that will split the genomic DNA into
#coding and non-coding parts, and
#write these sequences to two separate files.

#The first exon runs from the start of the
#sequence to the sixty-third character, and the second exon runs from the ninetyfirst
#character to the end of the sequence. Write a program that will print just the
#coding regions of the DNA sequence.
##############################################################################################


#1st I open the file with DNA sequence and save the file content in a variable
file = open("1. genomic_dna.txt")
dna_seq = file.read()
file.close()

#2nd I Split the sequence in the two exons and intron
exon1 = dna_seq[:63]
intron = dna_seq[63:90]
exon2 = dna_seq[90:]


#3th I open two new files where I will write the exons and intron saved before. I have to use the "w" flag to write.
#I the file does not exists it will be created automaticaly
coding_file = open("1. Result-coding_file.txt", "w")
nonCcoding_file = open("1. Result-intron_file.txt", "w")

#4th I write the exon1 and exon2 in their documents
coding_file.write(exon1 + exon2)
nonCcoding_file.write(intron)

#5th Finally, I close the new files
coding_file.close()
nonCcoding_file.close()


