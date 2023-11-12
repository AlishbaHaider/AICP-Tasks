departure_timings = [9,11,13,15]
return_timings = [10,12,14,16]
passengers_available = [480,480,480,640]
total_ticket_cash = [0,0,0,0]
def displayDepartureTimings():
    j = 0
    for i in departure_timings:
        print("train ", (j + 1), " -", i,":00")
        j = j + 1
def displayReturnTimings(dep_train):
    j = 0
    for i in return_timings:
        if departure_timings[dep_train-1]<i:
         print("train ", (j + 1), " -", i,":00")
        j=j+1
def displayDetails():
 print("---electric mountain railway---")
 for i in range(4):
    print("TRAIN ", i+1)
    print("departure time - ", departure_timings[i], ":00")
    print("return time - ", return_timings[i], ":00")
    print("seats available - ", passengers_available[i])
    print("total cash - ",total_ticket_cash[i])
    print("----------------------------------------")
def calculateTicketPrice(numOfSeats,dep_train,ret_train):
 if (numOfSeats>=10 and numOfSeats<=80):
    free = numOfSeats//10
    ticketPrice = (numOfSeats-free)*50
    total_ticket_cash[dep_train-1] = ticketPrice/2
    total_ticket_cash[ret_train-1] = ticketPrice/2
def maxPassengers():
    max=passengers_available[0]
    for i in passengers_available:
        if i<max:
            max=i
    return passengers_available.index(max)

while(True):
 print("welcome dear passenger :) \n press c to continue e to exit")
 choice = input()
 if (choice=='c'):
  print("enter number of tickets you want to book."
      "Special deal for groups with more than 10 people")
  print("cost of departure ticket(25$) + return ticket(25$) is 50$")
  numOfSeats = int(input())
  print("select the train for departure(1,2,3,4)")
  displayDepartureTimings()
  dep_train = int(input())
  if passengers_available[dep_train-1]>numOfSeats:
   passengers_available[dep_train-1]=passengers_available[dep_train-1]-numOfSeats
   while(True):
    print("select the train for return journey")
    displayReturnTimings(dep_train)
    ret_train = int(input())
    if(passengers_available[ret_train - 1] > numOfSeats):
      passengers_available[ret_train-1]=passengers_available[ret_train-1]-numOfSeats
      calculateTicketPrice(numOfSeats,dep_train,ret_train)
      break
    else:
       print("not enough seats available")
  else :
    print("not enough seats available")
  print("---updated info---")
  displayDetails()
 if (choice=='e'):
    print("operation ended!!")
    max = maxPassengers()
    print("train with highest number of passengers is train number",max+1)
    break


