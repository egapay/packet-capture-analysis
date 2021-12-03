from filter_packets import *
from packet_parser import *
from compute_metrics import *

node1 = []
node2 = []
node3 = []
node4 = []
nodes = []
FileName = "output.csv"

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

nodes.append(node1)
nodes.append(node2)
nodes.append(node3)
nodes.append(node4)

for i in range(0,4):
	if i == 0:
		SentReq, RecReq, SentRep, RecRep, TotalReqSent, TotalReqRec, DataReqSent, DataReqRec, rtt, throughput, avggoodput, avgrplydelay = compute(nodes[i], 1)
		csv = open(FileName, 'w')
		NodeInfo = ("Echo Requests Sent,Echo Requests Received,Echo Replies Sent,Echo Replies Receieved" + "\n" + str(SentReq) + "," + str(RecReq) + "," + str(SentRep) + "," + str(RecRep) + "\n" + 
					"Echo Request Bytes Sent (bytes),Echo Request Data Sent (bytes)" + "\n" + str(TotalReqSent) + "," + str(TotalReqRec) + "\n" +
					"Echo Request Bytes Received (bytes),Echo Request Data Received (bytes)" + "\n" + str(DataReqSent) + "," + str(DataReqRec) + "\n" + "\n" + "Average RTT (miliseconds)," + 
					str(rtt) + "\n" + "Echo Request Throughput (kB/sec)," + str(throughput) + "\n" + "Echo Request Goodput (kB/sec)," + str(avggoodput) + "\n" + "Average Reply Delay (microseconds)," + 
					str(avgrplydelay) + "\n" + "Average Echo Request Hop Count," + "num")
		csv.write(str("Node" + str(i + 1)) + "\n" + "\n" + NodeInfo + "\n" + "\n")
		csv.close()
	
	else:
		SentReq, RecReq, SentRep, RecRep, TotalReqSent, TotalReqRec, DataReqSent, DataReqRec, rtt, throughput, avggoodput, avgrplydelay = compute(nodes[i], 1)
		csv = open(FileName, 'a')
		NodeInfo = ("Echo Requests Sent,Echo Requests Received,Echo Replies Sent,Echo Replies Receieved" + "\n" + str(SentReq) + "," + str(RecReq) + "," + str(SentRep) + "," + str(RecRep) + "\n" + 
					"Echo Request Bytes Sent (bytes),Echo Request Data Sent (bytes)" + "\n" + str(TotalReqSent) + "," + str(TotalReqRec) + "\n" +
					"Echo Request Bytes Received (bytes),Echo Request Data Received (bytes)" + "\n" + str(DataReqSent) + "," + str(DataReqRec) + "\n" + "\n" + "Average RTT (miliseconds)," + 
					str(rtt) + "\n" + "Echo Request Throughput (kB/sec)," + str(throughput) + "\n" + "Echo Request Goodput (kB/sec)," + str(avggoodput) + "\n" + "Average Reply Delay (microseconds)," + 
					str(avgrplydelay) + "\n" + "Average Echo Request Hop Count," + "num")
		csv.write(str("Node" + str(i + 1)) + "\n" + "\n" + NodeInfo + "\n" + "\n")
		csv.close()
			

