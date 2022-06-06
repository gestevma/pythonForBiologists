#################################################################################
# Here's a short DNA sequence:
# ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT
# The sequence contains a recognition site for the EcoRI restriction enzyme, which
# cuts at the motif G*AATTC (the position of the cut is indicated by an asterisk).
# Write a program which will calculate the size of the two fragments that will be
# produced when the DNA sequence is digested with EcoRI.
#################################################################################


#We need to find the position of the motif.
#Once find it I will obtain two substrings from the beginning to the G of the motif (include)
#and a second substring after G of motif to final

dna_seq = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"

cut_position = dna_seq.find("GAATTC") #Obtain the position of motif, it gives the position of the first element (the G)

dna_forward_cut = dna_seq[:cut_position+1] #substring from beginnig to G of motif
dna_backward_cut = dna_seq[cut_position+1:] #Substring from motif (after G) to the end

print(len(dna_forward_cut))
print(len(dna_backward_cut))
