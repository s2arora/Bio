Code = {'TTT': 'F', 'TCT': 'S', 'TAT': 'Y', 'TGT': 'C',
        'TTC': 'F', 'TCC': 'S', 'TAC': 'Y', 'TGC': 'C',
        'TTA': 'L', 'TCA': 'S', 'TAA': '*', 'TGA': '*',
        'TTG': 'L', 'TCG': 'S', 'TAG': '*', 'TGG': 'W',
        'CTT': 'L', 'CCT': 'P', 'CAT': 'H', 'CGT': 'R',
        'CTC': 'L', 'CCC': 'P', 'CAC': 'H', 'CGC': 'R',
        'CTA': 'L', 'CCA': 'P', 'CAA': 'Q', 'CGA': 'R',
        'CTG': 'L', 'CCG': 'P', 'CAG': 'Q', 'CGG': 'R',
        'ATT': 'I', 'ACT': 'T', 'AAT': 'N', 'AGT': 'S',
        'ATC': 'I', 'ACC': 'T', 'AAC': 'N', 'AGC': 'S',
        'ATA': 'I', 'ACA': 'T', 'AAA': 'K', 'AGA': 'R',
        'ATG': 'M', 'ACG': 'T', 'AAG': 'K', 'AGG': 'R',
        'GTT': 'V', 'GCT': 'A', 'GAT': 'D', 'GGT': 'G',
        'GTC': 'V', 'GCC': 'A', 'GAC': 'D', 'GGC': 'G',
        'GTA': 'V', 'GCA': 'A', 'GAA': 'E', 'GGA': 'G',
        'GTG': 'V', 'GCG': 'A', 'GAG': 'E', 'GGG': 'G'
        }

while True:
	baseIn = input("Enter three-base codon to build: ")
	baseIn_C = baseIn.upper()
	
	if baseIn_C == "XXX":
		print ("Okay, I will stop.")
		break

	aminoIn = input("Enter amino acid: ")
	aminoIn_C = aminoIn.upper()
	
	Code[baseIn_C] = aminoIn_C

'''
	while True:
		baseS = input("Enter three-base codon to search: ")
		baseS_C = baseS.upper()
		print ("Amino acid for {}: {}".format(baseS_C,Code[baseS_C])
	
		if baseS_C == "XXX":
			print ("Okay, I will switch.")
			break
'''

