# Use the data from the previous exercise, but instead of creating a single FASTA file,
# create three new FASTA files – one per sequence. The names of the FASTA files
# should be the same as the sequence header names, with the extension .fasta.
# make sure that all sequences are in upper case and only contain the bases A, T, G
# and C.
#----------------------------------------------------------------------------
#------- Sequence header ----------           DNA Sequence           --------
#-------      ABC123     ---------- ATCGTACGATCGATCGATCGCTAGACGTATCG --------
#-------      DEF456     ----------   actgatcgacgatcgatcgatcacgact   --------
#-------      HIJ789     ----------  ACTGAC-ACTGT--ACTGTA----CATGTG  --------
#----------------------------------------------------------------------------


#I declare the sequences and headers
header1 = "ABC123"
sequence1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"

header2 = "DEF456"
sequence2 = "actgatcgacgatcgatcgatcacgact"

header3 = "HIJ789"
sequence3 = "ACTGAC-ACTGT--ACTGTA----CATGTG"

#Later, I open the files, the names will be the header.fasta, and they will be writable.
# How they have the "w" parameter, if the documents do not exist, they will be created
#The files will be created in the actual route
file1 = open(header1 + ".fasta", "w")
file2 = open(header2 + ".fasta", "w")
file3 = open(header3 + ".fasta", "w")

#The docuements are writed with header and sequence
#The sequences are written with conditions in the wording
file1.write(">" + header1 + "\n" + sequence1)
file2.write(">" + header2 + "\n" + sequence2.upper())
file3.write(">" + header3 + "\n" + sequence3.replace("-", ""))

#Finaly I close the files
file1.close()
file2.close()
file3.close()
