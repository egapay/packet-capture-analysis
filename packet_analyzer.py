from filter_packets import *
from packet_parser import *
from compute_metrics import *

filter()
parse(
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
)
compute()
