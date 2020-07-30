cnt = 0
ORIGIN_passed = False
Origin_trace = []

with open("sequence.protein.gb",'r') as fr:
	for line in fr:
		cnt += 1
		if cnt == 1:
			title = line 		
		if line.startswith("ORIGIN"):
			ORIGIN_passed = True
		elif ORIGIN_passed:
			Origin_trace.append(line.strip())
			
protein = ""
for protein_line in Origin_trace:
	protein += protein_line+"\n"


print("title:",title+
		"seq:",protein.strip())
