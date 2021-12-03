from typing import List


def compute(List, node) :
   #Metrics To Calculate
   i = 0
   String =  ' '
   SentReq = 0
   RecReq = 0
   SentRep = 0
   RecRep = 0
   TotalReqSent = 0
   TotalReqRec = 0
   DataReqSent = 0
   DataReqRec = 0
   source = 0
   RequestNo = 0
   RequestTime = 0
   ReplyNo = 0
   ReplyTime = 0
   corresponding = 1 #value to check for corresponding Echo Request and Reply
   rtt = 0
   TimeNano = 0
   counter=0
   goodput = 0
   delay = 0

   #Set Which Source IP to use based on what Node we getting info from
   if node == 1:
      source = "192.168.100.1"
   if node == 2:
      source = "192.168.100.2"
   if node == 3:
      source = "192.168.200.1"
   if node == 4:
      source = "192.168.200.2"
   reply = "reply"
   request = "request" 

   #For Loop To Iterate Through Info List
   for x in List:
      #Calculate The Amount of Requests Sent
      if List[i][2] == source and List[i][8] == request:
         SentReq = SentReq + 1 
         #Total Echo Requests Bytes Sent
         TotalReqSent =  TotalReqSent + int(List[i][5]) 
         DataReqSent =  DataReqSent + (int(List[i][5])-42)
         RequestNo = List[i][0]
         RequestTime = List[i][1]
         goodput += (float(List[i][5])-42)/1000

      #Calculate The Amount of Requests Recieved
      if List[i][3] == source and List[i][8] == request:
         TotalReqRec =  TotalReqRec + int(List[i][5]) 
         DataReqRec =  DataReqRec + (int(List[i][5])-42)
         RecReq = RecReq + 1
         RequestNo = List[i][0]
         RequestTime = List[i][1]
         if(int(List[i+1][0]) - int(List[i][0]) == corresponding):
            delay += (float(List[i+1][1]) - float(List[i][1])) * 1000000
            counter += 1
      #Calculate The Amount of Replies sent
      if List[i][2] == source and List[i][8] == reply:
         SentRep = SentRep + 1 
         ReplyNo = List[i][0]
         ReplyTime = List[i][1]

      #Calculate The Amount of Replies Recieved
      if List[i][3] == source and List[i][8] == reply:
         RecRep = RecRep + 1 

         ReplyNo = List[i][0]
         ReplyTime = List[i][1]

         if (int(ReplyNo) - int(RequestNo)) == corresponding:
            TimeNano = TimeNano + (float(ReplyTime) - float(RequestTime))
      i= i + 1

   #Average Ping Round Trip Time (RTT)
   rtt = round(((TimeNano / float(128)) / 0.001), 2)

   #Echo Request Throughput
   throughput = round((float(TotalReqSent)/float(TimeNano) * 0.001), 1)

   #Echo Request Goodput
   avggoodput = round(goodput/TimeNano, 1)

   #Average Reply Delay
   avgrplydelay = round(delay/counter, 2)

   print("Echo Request Sent: " + str(SentReq))	
   print("Echo Requests Recieved: " + str(RecReq))
   print("Echo Replies Sent: " + str(SentRep))
   print("Echo Replies Recieved: " + str(RecRep))
   print("Echo Request Bytes Sent: " + str(TotalReqSent))
   print("Echo Request Bytes Received: " + str(TotalReqRec))
   print("Echo Request Data Sent: " + str(DataReqSent))
   print("Echo Request Data Received: " + str(DataReqRec) + "\n")
   print("Average RTT (ms): " + str(rtt))
   print("Echo Request Throughput: " + str(throughput))
   print("Echo Request Goodput(kB/sec): " + str(avggoodput))
   print("Average Reply Delay(us): " + str(avgrplydelay) + "\n")
   print("Average Echo Request Hop Count: ")

   #Ideas for printing out to CSV file: Return all of the variables listed above, in packet_analyzer.py create, open, and write to file.
   return SentReq, RecReq, SentRep, RecRep, TotalReqSent, TotalReqRec, DataReqSent, DataReqRec, rtt, throughput, avggoodput, avgrplydelay
