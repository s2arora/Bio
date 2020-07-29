sequence = ""

with open("sequence.protein.2.fasta",'r') as fr:
	for line in fr:
		if line.startswith(">"):
			continue
		else:
			sequence += line.strip()

while True: 
	word = input("Searching: ")
	word = word.upper()

	if word == "XXX":
		print("Okay, I will stop.")
		break
	else:
		number = []
		num = 1
		
		for seq in sequence:
			if seq == word:
				number.append(str(num))
			num += 1
		print("Found at:",','.join(number))

#[number.append(seq.index(word)+1) for _ in seq]
#number += str(seq.index(word)+1)


