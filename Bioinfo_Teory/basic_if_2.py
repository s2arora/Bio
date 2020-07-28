
print 'Score Grade \n>=0.9 A \n>=0.8 B \n>=0.7 C \n>=0.6 D \n <0.6 F \n'
 
score = raw_input('Enter score: ')


try:
	ss = float(score)

	if 0.0 <= ss <= 1.0:	 
		if ss >= 0.9:
			print 'A'
		elif ss >= 0.8:
			print 'B'
		elif ss >= 0.7:
			print 'C'
		elif ss >= 0.6:
			print 'D'
		elif ss < 0.6:
			print 'F'
	else:
		print 'Bad score'
except:
	print 'Bad score'
