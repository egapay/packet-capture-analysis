def compute(List, node) :
  #Metrics To Calculate
  i = 0
  SentReq = 0
  RecReq = 0
  SentRep = 0
  RecRep = 0
  source = 0
  #Set Which Source IP to use based on what Node we getting info from
  if node == 1:
    source = "192.168.100.1"
  if node == 2:
    source = "192.168.100.2"
  if node == 3:
    source = "192.168.200.1"
  if node == 4:
    source = "192.168.200.2"
  reply = "Echo (ping) reply    id=0x0001"
  request = "Echo (ping) request id=0x0001" 
  #For Loop To Iterate Through Info List
  for x in List:
    #print(L[i][6] == reply)
    print(List[i][2] == source)
    #Calculate The Amount of Requests Sent
    if List[i][2] == source and List[i][6] == request:
     SentReq = SentReq + 1 
     print( "Amount of Requests Sent = " + str(SentReq))
    #Calculate The Amount of Requests Recieved
    if List[i][3] == source and List[i][6] == request:
     RecReq = RecReq + 1 
     print("Amount of Requests Recieved = " + str(RecReq))
    #Calculate The Amount of Replies sent
    if List[i][2] == source and List[i][6] == reply:
      SentRep = SentRep + 1 
      print("Amount of Replies Sent = " + str(SentRep))
    #Calculate The Amount of Replies Recieved
    if List[i][3] == source and List[i][6] == reply:
     RecRep = RecRep + 1 
     print("Amount of Replies Recieved = " + str(RecRep))

    print(List[i][2])
    i= i + 1	
  
  print(SentReq)
  print(RecReq)
  print(SentRep)
  print(RecRep)

  #print(str((float(List[0][5]) - 28)/(float(List[0][1]))))
  #Echo Request Goodput
  
  f = 0
  while f < len(List):
    if(List[f][8] == "request"): #checks to make sure that it is a request packet
      goodput = format(((float(List[f][5]) - 28)/1000)/(float(List[f][1])), ".5f") #sets the output variable to the length of the packet - 28 and divdes it by 1000 (kB/sec then divides it by the time
      print(goodput)
    f += 1
