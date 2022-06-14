# Write a program that will create a FASTA file for the following three sequences –
# make sure that all sequences are in upper case and only contain the bases A, T, G
# and C.
#----------------------------------------------------------------------------
#------- Sequence header ----------           DNA Sequence           --------
#-------      ABC123     ---------- ATCGTACGATCGATCGATCGCTAGACGTATCG --------
#-------      DEF456     ----------   actgatcgacgatcgatcgatcacgact   --------
#-------      HIJ789     ----------  ACTGAC-ACTGT--ACTGTA----CATGTG  --------
#----------------------------------------------------------------------------

#Define the header and sequence
header1 = "ABC123"
sequence1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"

header2 = "DEF456"
sequence2 = "actgatcgacgatcgatcgatcacgact"

header3 = "HIJ789"
sequence3 = "ACTGAC-ACTGT--ACTGTA----CATGTG"

#Later, I open the file, they will be writable.
# How they have the "w" parameter, if the documents do not exist, they will be created
#The files will be created in the actul route
file = open("2. Result-FASTA_file.fasta", "w")

#Write the header and sequene in the document creaded before
#The sequences are written with conditions in the wording
file.write(">" + header1 + "\n" + sequence1 + "\n")
file.write(">" + header2 + "\n" + sequence2.upper() + "\n")
file.write(">" + header3 + "\n" + sequence3.replace("-", ""))

#Close the file
file.close()

