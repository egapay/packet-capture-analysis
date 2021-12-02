from filter_packets import *
from packet_parser import *
from compute_metrics import *

node1 = []
node2 = []
node3 = []
node4 = []

filter("Node1.txt")
filter("Node2.txt")
filter("Node3.txt")
filter("Node4.txt")

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

compute(node1, 1)
