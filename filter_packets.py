def filter(file):
	#open file and read number of lines
	count_file = open(file, 'r')
	file_lines = count_file.readlines()
	num_lines = len(file_lines)
	count_file.close()

	#open file to read lines into output file
	input_file = open(file, 'r')
	#changing output file name based off original passed through file
	output_file_name = 'Node' + file[4:5] + '_filtered.txt'
	output_file = open(output_file_name, 'w')
	count = 0

	#read in file depending on amount of lines from file
	line = input_file.readline()
	while count < num_lines:
		#checks for keyword
		check = "ICMP"
		line.strip()
		if check in line:
			# if keyword exists, write out line to file
			output_file.write(line)
		line = input_file.readline()
		count += 1
	

filter("Node1.txt")
filter("Node2.txt")
filter("Node3.txt")
filter("Node4.txt")


