###################################################################################
#-----------------------------------Part 1----------------------------------------#
# Write a function that takes two arguments – a protein sequence and an amino acid
# residue code – and returns the percentage of the protein that the amino acid makes
# up. Use the following assertions to test your function:
####################################################################################

#Function that retorn the percentatge of aminoacid in a protein give them by parameter
def amino_acid_percentage (protein, amino_acid):
    
    #First I write the protein and amino acid (AA) in upper case
    protein = protein.upper()
    amino_acid = amino_acid.upper()
    
    protein_len = len(protein) #I need to know the number of total AAs in protein (or lenght)
    count_aminoacid = protein.count(amino_acid) #I need to know the number of times the AA appears
    
    amino_percentage = (count_aminoacid/protein_len)*100 #I calculate the percentaje of aminoacid in that protein
    
    return amino_percentage #Finally, I return the result


#I check the function with assert. I give the theorical result. If the result of the function and the result I write are the same the programm will be executed normaly
#If there are a mistake it'll gives an error
assert amino_acid_percentage("MSRSLLLRFLLFLLLLPPLP", "M") == 5
assert amino_acid_percentage("MSRSLLLRFLLFLLLLPPLP", "r") == 10
assert amino_acid_percentage("MSRSLLLRFLLFLLLLPPLP", "Y") == 0



####################################################################################
#----------------------------------Part 2------------------------------------------#
# Modify the function from part one so that it accepts a list of amino acid residues
# rather than a single one. If no list is given, the function should return the
# percentage of hydrophobic amino acid residues (A, I, L, M, F, W, Y and V). Your
# function should pass the following assertions:
#####################################################################################

#I define a list of aminoacids that I use by default in function
hidrophobic_amino_acids = ["A", "I", "L", "M", "F", "W", "Y", "V"]

#Define the function. This time I want to return the percentage of a list of aminoacids in a protein
#I define a default value for the list of aminoacids 
def amino_acid_percentage2 (protein, amino_acid_list = hidrophobic_amino_acids):
    protein = protein.upper()
    protein_len = len(protein)
    
    #I count the total times that appears every AA. for that I need to make a for to count every
    # AA of the list individualy
    total_aa_count = 0
    for amino_acid in amino_acid_list:
        amino_acid = amino_acid.upper()
        amino_acid_count = protein.count(amino_acid)
        total_aa_count = total_aa_count + amino_acid_count
    
    amino_percentage = (total_aa_count/protein_len)*100 #I calculate the percentatge with all aminoacids in the list
    
    return amino_percentage #I return the result


#Finally I check the result with assert
assert amino_acid_percentage2("MSRSLLLRFLLFLLLLPPLP", ["M"]) == 5
assert amino_acid_percentage2("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']) == 70
assert amino_acid_percentage2("MSRSLLLRFLLFLLLLPPLP") == 65