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
         DataReqSent =  DataReqSent + (int(List[i][5])-32)

         RequestNo = List[i][0]
         RequestTime = List[i][1]

      #Calculate The Amount of Requests Recieved
      if List[i][3] == source and List[i][8] == request:
         TotalReqRec =  TotalReqRec + int(List[i][5]) 
         DataReqRec =  DataReqRec + (int(List[i][5])-32)
         RecReq = RecReq + 1

      #Calculate The Amount of Replies sent
      if List[i][2] == source and List[i][8] == reply:
         SentRep = SentRep + 1 

      #Calculate The Amount of Replies Recieved
      if List[i][3] == source and List[i][8] == reply:
         RecRep = RecRep + 1 

         ReplyNo = List[i][0]
         ReplyTime = List[i][1]

         if (int(ReplyNo) - int(RequestNo)) == corresponding:
            TimeNano = TimeNano + (float(ReplyTime) - float(RequestTime))
      

      
      i= i + 1

   rtt = round(((TimeNano / float(128)) / 0.001), 2) #needs to be edited, not sure if in ms
   print( "Amount of Requests Sent = " + str(SentReq))	
   print("Amount of Requests Recieved = " + str(RecReq))
   print("Amount of Replies Sent = " + str(SentRep))
   print("Amount of Replies Recieved = " + str(RecRep))

   print(TotalReqSent)
   print(TotalReqRec)
   print(DataReqSent)
   print(DataReqRec)
   print("RTT = " + str(rtt))


