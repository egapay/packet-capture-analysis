def filter(input_file):
	file1 = open(input_file, 'r')
	file_lines = file1.readlines()
	print(file_lines)
	num_lines = len(file_lines)
	print(num_lines)
	line = file1.readline()
	i = 0
	while i < num_lines:
		word = "ICMP"
		line = line.strip()
		line = file1.readline().strip()
		if i < 20:
			print(line)
		i = i + 1
		if word in line:
			print(line)
	

filter("Node1.txt");


