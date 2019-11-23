

words_file = 'data/monty_python_keywords.txt'
try:
	f = open(words_file)
	line = f.readline()
	while line != '':
		if line == 'semprini\n':
			print('A semprini has been detected in the file')
			break
		line = f.readline()
	f.close()	
except IOError:
	print("Cannot find file: " + words_file)