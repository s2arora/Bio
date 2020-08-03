def line_70_cut(string, cnt=70) :
    count = 0
    temp = ""
    seq_list = []
    for c in string:
        count += 1
        temp += c
        if count % cnt == 0:
            seq_list.append(temp)
            temp = ""
    seq_list.append(temp)
    return seq_list

input_fileName = input("Enter input file: ")
make_fileName = input("Enter output file: ")

print("Option-1) Read a FASTA format DNA sequence file and make a reverse sequence")
print("Option-2) Read a FASTA format DNA sequence file and make a reverse complement")
print("Option-3) Convert GenBank format file to FASTA format file.")

select = int(input("Select the option: "))
if input_fileName == "sequence.nucleotide.fasta":    
    with open(input_fileName,"r") as fr:
        seq = ""
        for line in fr:
            if line.startswith(">"):
                title = line
            else:
                seq += line.strip()

    sequence_reversed = ''.join(reversed(seq))
    
    if select == 1:
        seq_list = line_70_cut(sequence_reversed)
        sequence1 = title + ('\n'.join(seq_list)) + "\n"
        with open(make_fileName, 'w') as fw:
            fw.write(sequence1)

    sequence_ATGC = {"A": "T",
                    "T": "A",
                    "G": "C",
                    "C": "G"}

    sequence_reversed_complement = ""
    if select == 2:
        for seq_rev in sequence_reversed:
            sequence_reversed_complement += sequence_ATGC[seq_rev]
        seq_list = line_70_cut(sequence_reversed_complement)
        sequence2 = title + ('\n'.join(seq_list)) + "\n"
        with open(make_fileName, 'w') as fw:
            fw.write(sequence2)


elif input_fileName == "sequence.nucleotide.gb":    
    seq = []
    origin_flag = False

    with open(input_fileName,"r") as fr:
        for line in fr:
            if line.startswith("LOCUS"):
                title = line

            if line.startswith("ORIGIN"):
                origin_flag = True 
            elif origin_flag:
                seq.append(line[10:-1])

    if select == 3:
        sequence = ""
        for sequence_line in seq:
            sequence += sequence_line.replace(" ", '')
        seq_list = line_70_cut(sequence)
        sequence3 = title + ('\n'.join(seq_list)) + "\n"

        with open(make_fileName,'w') as fw:
            fw.write(sequence3)            
