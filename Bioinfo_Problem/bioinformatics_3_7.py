seq = ""

with open("sequence.protein.2.fasta",'r') as fr:
	for line in fr:
		if line.startswith(">"):
			continue
		else:
			seq += line.strip()

while True: 
	position = input("Position: ")
	if position == "XXX":
		print("Okay, I will stop.")
		break
	else:
		seq_len = len(seq)
		try:
			position = int(position)
		except:
			print ("Please input Position nummber")
			continue
		if 1 <= position <= seq_len-3:
			sliced_seq = seq[position-1:position+2]
			print("Three amino acids: "+sliced_seq)
		else:
			print("Invalid range position value")

