fr = open("title.txt",'r')

line = fr.read()
line2 = line.strip()

print ("The first line is:",line2)

fr.close()
