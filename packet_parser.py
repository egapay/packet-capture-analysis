def parse(afile, data):
	infile = open(afile, 'r')

	line = infile.readline().strip()
	while line:
		test = ' '.join(line.split())		
		data.append(test.split(' '))	
		line = infile.readline().strip()
		
	infile.close()
	
	
	




