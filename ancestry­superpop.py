#Input genome, output superpopulation fractions to a .tab file.
#use argparse to input the files 


#TODO: learn what super popultion fractions are
#TODO: learn what a .tab file is
#TODO: what is the difference between a superpopulation and a subpopulation
#TODO: get the genomic information that we are going to use. is it fasta? can 
#we use lib functions we already have to parse this data?

#TODO: create git hub repo for this script 
#TODO: what is the difference between phased and unphased data
#TODO: what is a hapmap?
#TODO: what is an rs number? SNP?

#TODO: this might take some time, look into batch submission at duke
#also probably going to need to use numpy/scipy when creating these scripts

#what this script will do is call the scripts from the tutorial, and pass in the appropriate
#files

import argparse
if __name__ == "__main__": 
parser = argparse.ArgumentParser(description="Take in sample genome, output superpopulation csv file")
parser.add_argument("sample_genome", help = ".txt file with the raw genome of the person we want to run admixture on")
args = parser.parse_args()
print(args)

def ancestry_super_pop(args): 
	'''Input genome, output superpopulation fractions to a .tab file.
		use argparse to input the files'''