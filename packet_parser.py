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
	
	
	

node1 = []
node2 = []
node3 = []
node4 = []

for i in range(0, 3):
	if(i == 0):
		#afile = 'Node{}_filtered.txt'.format(i)
		afile = 'test.txt'
		parse(afile, node1)
	#if(i == 1):
		#afile = 'Node{}_filtered.txt'.format(i)
		#parse(afile, node2)
	#if(i == 2):
		#afile = 'Node{}_filtered.txt'.format(i)
		#parse(afile, node3)
	#if(i == 3):
		#afile = 'Node{}_filtered.txt'.format(i)
		#parse(afile, node4)
print(node1[0][6])
