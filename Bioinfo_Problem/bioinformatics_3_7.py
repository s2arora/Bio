seq = ""

with open("sequence.protein.2.fasta",'r') as fr:
	for line in fr:
		if line.startswith(">"):
			continue
		else:
			seq += line.strip()

while True: 
	num = input("Position: ")
	if num == "XXX":
		print("Okay, I will stop.")
		break
	print("Three amino acids: "+seq[int(num)-1:int(num)+2])

