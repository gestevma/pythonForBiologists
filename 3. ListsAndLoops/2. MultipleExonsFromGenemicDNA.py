# The file genomic_dna.txt contains a section of genomic DNA, and the file exons.txt
# contains a list of start/stop positions of exons. Each exon is on a separate line and
# the start and stop positions are separated by a comma. Write a program that will
# extract the exon segments, concatenate them, and write them to a new file.

#Open the files
dna_sequence_file = open("genomic_dna.txt")
dna_sequence = dna_sequence_file.read()
exons_positions = open("exons.txt")

#Save a variable where I will concat the exons from the coding dna
coding_dna = ""

#I loop the file exons_positions, on each loop the variable exon_pos will have
#one line of the file that corresponds to the first and last position of the exons
for exon_pos in exons_positions:
    
    #Split the lines to have just the numbers of positions
    list_exon_pos = exon_pos.split(",") 
    
    #Save the start and end position of exons and transform in numbers. 
    #I make -1 in the begin exon because an string in python starts in 0
    #I don't have tho make -1 in finish exon because the final position will not be included
    exon_begin = int(list_exon_pos[0]) - 1
    exon_end = int(list_exon_pos[1])

    #I concat the actual content of coding_dna with the sequence (of file dna_sequence)
    # cutting from start position to end position (not included)
    coding_dna = coding_dna + dna_sequence[exon_begin:exon_end]

#create a new file to save the coding_dna
coding_dna_file = open("2. Coding_DNA_file.txt", "w")
coding_dna_file.write(coding_dna)

print(len(coding_dna))
#Close the files
dna_sequence_file.close()
exons_positions.close()
coding_dna_file.close()
