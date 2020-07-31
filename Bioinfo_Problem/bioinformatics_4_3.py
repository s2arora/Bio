ORIGIN_passed = False
Origin_trace = []

with open("sequence.protein.gb",'r') as fr:
	for line in fr:
		if line.startswith("ORIGIN"):
			ORIGIN_passed = True
		elif ORIGIN_passed:
			Origin_trace.append(line[10:-1])

#Origin_trace is protein line list [have a space]

protein_word = ""
for protein_line in Origin_trace:
	protein_word += protein_line.replace(" ",'')

count = 0

for i in protein_word:
	print (i, end= '')
	count += 1
	if count == 70:
		print("")
		count = 0

print("")