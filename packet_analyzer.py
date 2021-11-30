from filter_packets import *
from packet_parser import *
from compute_metrics import *

filter("Node1.txt")
filter("Node2.txt")
filter("Node3.txt")
filter("Node4.txt")

parse()
compute()
