def parse(afile, data):
	print('called parse function in packet_parser.py')
	infile = open(afile, 'r')

	line = infile.readline().strip()
	x = 0
	while line:
		test = ' '.join(line.split())		
		data.append(test.split(' '))	
		line = infile.readline().strip()
		
	infile.close()
	
	
	




