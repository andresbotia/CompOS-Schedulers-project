Process = [
            [5, 27, 3, 31, 5, 43, 4, 18, 6, 22, 4, 26, 3, 24, 4],
            [4, 48, 5, 44, 7, 42, 12, 37, 9, 76, 4, 41, 9, 31, 7, 43, 8],
            [8, 33, 12, 41, 18, 65, 14, 21, 4, 61, 15, 18, 14, 26, 5, 31, 6],
            [3, 35, 4, 41, 5, 45, 3, 51, 4, 61, 5, 54, 6, 82, 5, 77, 3],
            [16, 24, 17, 21, 5, 36, 16, 26, 7, 31, 13, 28, 11, 21, 6, 13, 3, 11, 4],
            [11, 22, 4, 8, 5, 10, 6, 12, 7, 14, 9, 18, 12, 24, 15, 30, 8],
            [14, 46, 17, 41, 11, 42, 15, 21, 4, 32, 7, 19, 16, 33, 10],
            [4, 14, 5, 33, 6, 51, 14, 73, 16, 87, 6]
           ]
class FCFS:
    Turn = 0
    Tw = 0
    Tr = 0
    length = 0
    Sum = 0
    Cpu = 0
running = []
ready = []
io = []
terminate = []
a = 0
b = 0
c = 0
e = 0
Ttr = 0


Pr1 = FCFS() #setting each process accordingly to its data, their own wait time, turnaround time, response time, etc
Pr2 = FCFS()
Pr3 = FCFS()
Pr4 = FCFS()
Pr5 = FCFS()
Pr6 = FCFS()
Pr7 = FCFS()
Pr8 = FCFS()
Average = FCFS()

P1 = Process[0] #a reference pointer to track the array that is in progress
P2 = Process[1]
P3 = Process[2]
P4 = Process[3]
P5 = Process[4]
P6 = Process[5]
P7 = Process[6]
P8 = Process[7]

Pr1.length = len(Process[0]) 
Pr2.length = len(Process[1])
Pr3.length = len(Process[2])
Pr4.length = len(Process[3])
Pr5.length = len(Process[4])
Pr6.length = len(Process[5])
Pr7.length = len(Process[6])
Pr8.length = len( Process[7])
def average(): #gets the avg for turnaround time,response time, cpu burst, and total run time
    Average.Tr = (Pr1.Tr + Pr2.Tr + Pr3.Tr + Pr4.Tr + Pr5.Tr + Pr6.Tr + Pr7.Tr + Pr8.Tr)/8 
    Average.Turn = (Pr1.Turn + Pr2.Turn + Pr3.Turn + Pr4.Turn + Pr5.Turn + Pr6.Turn + Pr7.Turn + Pr8.Turn)/8
    Average.Tw = (Pr1.Tw + Pr2.Tw + Pr3.Tw + Pr4.Tw + Pr5.Tw + Pr6.Tw + Pr7.Tw + Pr8.Tw)/8
    Average.Sum = (Pr1.Sum + Pr2.Sum + Pr3.Sum + Pr4.Sum + Pr5.Sum + Pr6.Sum + Pr7.Sum + Pr8.Sum)/8
def Sum():
    i = 0
    while i < len(Process[0]):
        Pr1.Sum += Process[0][i]
        i +=1
    i = 0
    while i < len(Process[1]):
        Pr2.Sum += Process[1][i]
        i +=1
    i = 0
    while i < len(Process[2]):
        Pr3.Sum += Process[2][i]
        i +=1
    i = 0
    while i < len(Process[3]):
        Pr4.Sum += Process[3][i]
        i +=1
    i = 0
    while i < len(Process[4]):
        Pr5.Sum += Process[4][i]
        i +=1
    i = 0
    while i < len(Process[5]):
        Pr6.Sum += Process[5][i]
        i +=1
    i = 0
    while i < len(Process[6]):
        Pr7.Sum += Process[6][i]
        i +=1
    i = 0
    while i < len(Process[7]):
        Pr8.Sum += Process[7][i]
        i +=1
Sum()
def waiting(): #used for finding wait time
    Pr1.Tw = Pr1.Turn - Pr1.Sum
    Pr2.Tw = Pr2.Turn - Pr2.Sum
    Pr3.Tw = Pr3.Turn - Pr3.Sum
    Pr4.Tw = Pr4.Turn - Pr4.Sum
    Pr5.Tw = Pr5.Turn - Pr5.Sum
    Pr6.Tw = Pr6.Turn - Pr6.Sum
    Pr7.Tw = Pr7.Turn - Pr7.Sum
    Pr8.Tw = Pr8.Turn - Pr8.Sum
def Response(Ttr): #if the progress is running and length hasnt changed sets response time to turnaround time
    if P1 is running[0]:
        if Pr1.length == len(running[0]):
            Pr1.Tr = Ttr
    if P2 is running[0]:
         if Pr2.length == len(running[0]):
            Pr2.Tr = Ttr
    if P3 is running[0]:
         if Pr3.length == len(running[0]):
            Pr3.Tr = Ttr
    if P4 is running[0]:
         if Pr4.length == len(running[0]):
            Pr4.Tr = Ttr
    if P5 is running[0]:
         if Pr5.length == len(running[0]):
            Pr5.Tr = Ttr
    if P6 is running[0]:
         if Pr6.length == len(running[0]):
            Pr6.Tr = Ttr
    if P7 is running[0]:
         if Pr7.length == len(running[0]):
            Pr7.Tr = Ttr
    if P8 is running[0]:
        if Pr8.length == len(running[0]):
            Pr8.Tr = Ttr



def finished(): #prints a finished statement when a process is completed
            if len(P1) == 0:
                print("==============")
                print("P1 is finished")
                print("==============")
            if len(P2) == 0:
                print("==============")
                print("P2 is finished")
                print("==============")
            if len(P3) == 0:
                print("==============")
                print("P3 is finished")
                print("==============")
            if len(P4) == 0:
                print("==============")
                print("P4 is finished")
                print("==============")
            if len(P5) == 0:
                print("==============")
                print("P5 is finished")
                print("==============")
            if len(P6) == 0:
                print("==============")
                print("P6 is finished")
                print("==============")
            if len(P7) == 0:
                print("==============")
                print("P7 is finished")
                print("==============")
            if len(P8) == 0:
                print("==============")
                print("P8 is finished")
                print("==============")
                 
def counter(Ttr): #counter used for turnaround time
            if  len(P1) != 0:
                Pr1.Turn += 1
            if  len(P2) != 0:
                Pr2.Turn += 1
            if  len(P3) != 0:
                Pr3.Turn += 1
            if  len(P4) != 0:
                Pr4.Turn += 1
            if  len(P5) != 0:
                Pr5.Turn += 1
            if len(P6) != 0:
                Pr6.Turn += 1
            if len(P7) != 0:
                Pr7.Turn += 1
            if len(P8) != 0:
                Pr8.Turn += 1
         

def IoCount(io,ready, Ttr): #runs the io
    i = 0
    d = 0
    while i < len(io): #loops through io
        if(len(io[i])==0): 
            finished() #prints finished statements if there is any
            terminate.append(io.pop(i)) #removes process from cycle
            continue 
        elif(len(io[i]) > 0): #checks if there is any values remaining
            io[i][0] -=1 #decrements the first value
            i +=1
    while d < len(io): #iterates through the values of io
        if(io[d][0] <= 0): 
            new_word = io[d]
            new_word.pop(0)
            ready.append(io.pop(d))
        d +=1

while a < 8:
    ready.append(Process[a]) #moves all the processes into ready
    a +=1
while(ready or running or io):
    if(not running): #checks if running is empty
        if(ready): #if ready has any values
            running.append(ready.pop(b)) #adds to running
            if(running): 
                Response(Ttr) #assigns to response time
                print("Running List:") #shows all values in running
                print(running[0])
            else:
                print("Running burst is empty")
            if(ready): 
                c = 0
                print("Ready List:")
                while c < len(ready):
                    print(ready[c])
                    c +=1
            else:
                print("Ready is empty")
            if(io): 
                c = 0
                print("IO burst:")
                while c < len(io):
                    print(io[c])
                    c +=1
            else: 
                print("IO is empty")
            running[0][0] -=1  
            Ttr +=1
            counter(Ttr)

    else:
        if(running[0][0] > 0): #if current running burts is greater than 0 than decrements it and increases turnaround time as well
            running[0][0]-=1
            Ttr +=1
   
        else:
            new_word = running[0] #removes the burst time from the current process when empty
            new_word.pop(0)
            io.append(running.pop()) 
        if(ready and not running):
            running.append(ready.pop(b)) 
            if(running): 
                Response(Ttr) 
                print("Running List:")
                print(running[0])
            else:
                print("Running burst is empty")
            if(ready):
                c = 0
                print("Ready List:")
                while c < len(ready):
                    print(ready[c])
                    c +=1
            else:
                print("Ready is empty")
            if(io): 
                c = 0
                print("IO burst:")
                while c < len(io):
                    print(io[c])
                    c +=1
            else: 
                print("IO is empty")
            running[0][0] -=1 
            Ttr +=1
    if(io):
        IoCount(io,ready, Ttr) #decrements all values in io
        counter(Ttr)
waiting()
average()
print(terminate)
print(Ttr)
usage = (Average.Turn/Ttr)*100


print()
print()
print()
print()
print("FCFS")
print("CPU Utilization = ", usage)
print("P1 | TTR:", Pr1.Turn,"| Tr:",Pr1.Tr,"| Tw:",Pr1.Tw," |")
print("P2 | TTR:", Pr2.Turn,"| Tr:",Pr2.Tr,"| Tw:",Pr2.Tw," |")
print("P3 | TTR:", Pr3.Turn,"| Tr:",Pr3.Tr,"| Tw:",Pr3.Tw," |")
print("P4 | TTR:", Pr4.Turn,"| Tr:",Pr4.Tr,"| Tw:",Pr4.Tw," |")
print("P5 | TTR:", Pr5.Turn,"| Tr:",Pr5.Tr,"| Tw:",Pr5.Tw," |")
print("P6 | TTR:", Pr6.Turn,"| Tr:",Pr6.Tr,"| Tw:",Pr6.Tw," |")
print("P7 | TTR:", Pr7.Turn,"| Tr:",Pr7.Tr,"| Tw:",Pr7.Tw," |")
print("P8 | TTR:", Pr8.Turn,"| Tr:",Pr8.Tr,"| Tw:",Pr8.Tw," |")
print("Average TTR = ", Average.Turn)
print("Average Tr = ", Average.Tr)
print("Average Tw = ", Average.Tw)
