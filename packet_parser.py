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

for i in range(1, 5):
	if(i == 1):
		afile = 'Node{}_filtered.txt'.format(i)
		parse(afile, node1)
	if(i == 2):
		afile = 'Node{}_filtered.txt'.format(i)
		parse(afile, node2)
	if(i == 3):
		afile = 'Node{}_filtered.txt'.format(i)
		parse(afile, node3)
	if(i == 4):
		afile = 'Node{}_filtered.txt'.format(i)
		parse(afile, node4)
print(node4[0][0])
