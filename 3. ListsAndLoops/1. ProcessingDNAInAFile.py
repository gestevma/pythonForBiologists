# The file input.txt contains a number of DNA sequences, one per line. Each sequence
# starts with the same 14 base pair fragment – a sequencing adapter that should have
# been removed. Write a program that will (a) trim this adapter and write the cleaned
# sequences to a new file and (b) print the length of each sequence to the screen.

#Open the input file and the file where write the cleaned sequence
dna_sequences = open("input.txt")
new_file = open("1. cleaned_DNA_Sequence.txt", "w")

#Loop in each line of the dna_sequences
for dna_seq in dna_sequences:

    #Save the sequece from position 15 to end (from 14 in python because starts in 0)
    clean_dna_seq = dna_seq[14:]
    
    #Add the sequence when the first 14 nucleotides has been removed
    new_file.write(clean_dna_seq)
    
    print(len(clean_dna_seq))
    
new_file.close()