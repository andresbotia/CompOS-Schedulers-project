Process = [
            [5,  27, 3,  31, 5,  43, 4,  18, 6,  22, 4,  26, 3,  24, 4],
            [4,  48, 5,  44, 7,  42, 12, 37, 9,  76, 4,  41, 9,  31, 7,  43, 8],
            [8,  33, 12, 41, 18, 65, 14, 21, 4,  61, 15, 18, 14, 26, 5,  31, 6],
            [3,  35, 4,  41, 5,  45, 3,  51, 4,  61, 5,  54, 6,  82, 5,  77, 3],
            [16, 24, 17, 21, 5,  36, 16, 26, 7,  31, 13, 28, 11, 21, 6,  13, 3, 11, 4],
            [11, 22, 4,  8,  5,  10, 6,  12, 7,  14, 9,  18, 12, 24, 15, 30, 8],
            [14, 46, 17, 41, 11, 42, 15, 21, 4,  32, 7,  19, 16, 33, 10],
            [4,  14, 5,  33, 6,  51, 14, 73, 16, 87, 6]
           ]
class MLFQ:
    Turn = 0
    Tw = 0
    Tr = 0
    Sum = 0
    Cpu = 0
running = [] #creates a running queue
RR1 = [] #creates a queue for round robin1
RR2 =[] #creates a queue for round robin2
FCFS = [] #creates a queue for fcfs
state1 = 0 #tracks which queue is in progress and how long its taking
state2 = 0
io = [] #creates io queue
current = 0
terminate = []
a = 0
b = 0
c = 0
e = 0
Ttr = 0

Pr1 = MLFQ()#setting each process accordingly to its data, their own wait time, turnaround time, response time, etc
Pr2 = MLFQ()
Pr2 = MLFQ()
Pr3 = MLFQ()
Pr4 = MLFQ()
Pr5 = MLFQ()
Pr6 = MLFQ()
Pr7 = MLFQ()
Pr8 = MLFQ()
Average = MLFQ()

P1 = Process[0]#a reference pointer to track the array that is in progress
P2 = Process[1]
P3 = Process[2]
P4 = Process[3]
P5 = Process[4]
P6 = Process[5]
P7 = Process[6]
P8 = Process[7]

Pr1.Tr = 0 
Pr2.Tr = 5
Pr3.Tr = 9
Pr4.Tr = 17
Pr5.Tr = 20
Pr6.Tr = 36
Pr7.Tr = 47
Pr8.Tr = 61
def average(): #gets the avg for turnaround time,response time, cpu burst, and total run time
    Average.Tr = (Pr1.Tr + Pr2.Tr + Pr3.Tr + Pr4.Tr + Pr5.Tr + Pr6.Tr + Pr7.Tr + Pr8.Tr)/8
    Average.Turn = (Pr1.Turn + Pr2.Turn + Pr3.Turn + Pr4.Turn + Pr5.Turn + Pr6.Turn + Pr7.Turn + Pr8.Turn)/8
    Average.Tw = (Pr1.Tw + Pr2.Tw + Pr3.Tw + Pr4.Tw + Pr5.Tw + Pr6.Tw + Pr7.Tw + Pr8.Tw)/8
    Average.Sum = (Pr1.Sum + Pr2.Sum + Pr3.Sum + Pr4.Sum + Pr5.Sum + Pr6.Sum + Pr7.Sum + Pr8.Sum)/8

def Sum():#gets total burst
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

def finished():  #prints a finished statement when a process is completed
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

def counter(Ttr): #increments ttr time
            if  len(P1) != 0:
                Pr1.Turn += 1
            if  len(P2) != 0:
                Pr2.Turn += 1
            if  len(P3) != 0:
                Pr3.Turn += 1
            if len(P4) != 0:
                Pr4.Turn += 1
            if  len(P5) != 0:
                Pr5.Turn += 1
            if len(P6) != 0:
                Pr6.Turn += 1
            if len(P7) != 0:
                Pr7.Turn += 1
            if len(P8) != 0:
                Pr8.Turn += 1
         

def IoCount(io,ready, Ttr):#runs io
    i = 0
    d = 0
    while i < len(io):#loops through the processes in io
        if(len(io[i])==0):#if the process is complete 
            finished() #prints the process is finished
            terminate.append(io.pop(i))  #removes the process from the cycle
            continue 
        elif(len(io[i]) > 0): 
            io[i][0] -=1 
            i +=1
    while d < len(io): #checks through the values of io
        if(io[d][0] <= 0): #if any values equal 0 move to rr1
            new_word = io[d]
            new_word.pop(0)
            RR1.append(io.pop(d))
        d +=1

while a < 8: #moves all processes into rr1
    RR1.append(Process[a])
    a +=1
while(RR1 or RR2 or FCFS or running or io):
    if(not running):
        if(RR1): 
            if(not running): 
                running.append(RR1.pop(b))#move the first value of rr1 into running
            if(running): 
                print("Running List:")
                print(running)
            else:
                print("Running burst is empty")
            if(RR1):
                c = 0
                print("RR1 List:")
                while c < len(RR1):
                    print(RR1[c][0])
                    c +=1
            else:
                print("RR1 is empty")
            if(RR2):
                c = 0
                print("RR2 List:")
                while c < len(RR2):
                    print(RR2[c][0])
                    c +=1
            else:
                print("RR2 is empty")
            if(FCFS):
                c = 0
                print("FCFS List:")
                while c < len(FCFS):
                    print(FCFS[c][0])
                    c +=1
            else:
                print("FCFS is empty")
            if(io):
                c = 0
                print("IO burst:")
                while c < len(io):
                    print(io[c])
                    c +=1
            else: 
                print("IO is empty")
            running[0][0] -=1 
            state1 +=1 
            current = 0 
            Ttr +=1
            counter(Ttr)
        elif(RR2):
            if(not running):
                running.append(RR2.pop(b))
            if(running):
                print("Running List:")
                print(running)
            else:
                print("Running burst is empty")
            if(RR1):
                c = 0
                print("RR1 List:")
                while c < len(RR1):
                    print(RR1[c][0])
                    c +=1
            else:
                print("RR1 is empty")
            if(RR2):
                c = 0
                print("RR2 List:")
                while c < len(RR2):
                    print(RR2[c][0])
                    c +=1
            else:
                print("RR2 is empty")
            if(FCFS):
                c = 0
                print("FCFS List:")
                while c < len(FCFS):
                    print(FCFS[c][0])
                    c +=1
            else:
                print("FCFS is empty")
            if(io):
                c = 0
                print("IO burst:")
                while c < len(io):
                    print(io[c])
                    c +=1
            else: 
                print("IO is empty")
            running[0][0] -=1
            state2 +=1
            current = 1
            Ttr +=1
            counter(Ttr)
        elif(FCFS):
            if(not running):
                running.append(FCFS.pop(b))
            if(running):
                print("Running List:")
                print(running[0][0])
            else:
                print("Running burst is empty")
            if(RR1):
                c = 0
                print("RR1 List:")
                while c < len(RR1):
                    print(RR1[c][0])
                    c +=1
            else:
                print("RR1 is empty")
            if(RR2):
                c = 0
                print("RR2 List:")
                while c < len(RR2):
                    print(RR2[c][0])
                    c +=1
            else:
                print("RR2 is empty")
            if(FCFS):
                c = 0
                print("FCFS List:")
                while c < len(FCFS):
                    print(FCFS[c][0])
                    c +=1
            else:
                print("FCFS is empty")
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
            current = 2
            counter(Ttr)
     
    else:
        if(running[0][0] > 0 and state1 < 5 and state2 < 10): #if running is greater than 0, rr1 is still less than 5, and rr2 is still less than 10
            running[0][0]-=1 
            print("current running:" , running[0][0])
            Ttr +=1
            if(current==0): #increments state depending on which queue its in
                state1+=1 
            elif(current==1):
                state2+=1
        else:
            state1 = state2 = 0 #resets tracker
            if(running[0][0] <= 0): #moves the value into io if its done
                new_word = running[0]
                new_word.pop(0)
                io.append(running.pop())
            elif(current == 0): #if the value isnt finished and has done 5 ticks moves to rr2
                RR2.append(running.pop())
            elif(current == 1): #if value isnt finished and has done 10 ticks it moves to FCFS
                FCFS.append(running.pop())
        if(RR1):
            if(not running):
                 running.append(RR1.pop(b))
            if(running):
                print("Running List:")
                print(running)
            else:
                print("Running burst is empty")
            if(RR1):
                c = 0
                print("RR1 List:")
                while c < len(RR1):
                    print(RR1[c][0])
                    c +=1
            else:
                print("RR1 is empty")
            if(RR2):
                c = 0
                print("RR2 List:")
                while c < len(RR2):
                    print(RR2[c][0])
                    c +=1
            else:
                print("RR2 is empty")
            if(FCFS):
                c = 0
                print("FCFS List:")
                while c < len(FCFS):
                    print(FCFS[c][0])
                    c +=1
            else:
                print("FCFS is empty")
            if(io):
                c = 0
                print("IO burst:")
                while c < len(io):
                    print(io[c])
                    c +=1
            else: 
                print("IO is empty")
            running[0][0] -=1
            state1 +=1
            current = 0
            Ttr +=1
     

        elif(RR2):
            if(not running):
                running.append(RR2.pop(b))
            if(running):
                print("Running List:")
                print(running)
            else:
                print("Running burst is empty")
            if(RR1):
                c = 0
                print("RR1 List:")
                while c < len(RR1):
                    print(RR1[c][0])
                    c +=1
            else:
                print("RR1 is empty")
            if(RR2):
                c = 0
                print("RR2 List:")
                while c < len(RR2):
                    print(RR2[c][0])
                    c +=1
            else:
                print("RR2 is empty")
            if(FCFS):
                c = 0
                print("FCFS List:")
                while c < len(FCFS):
                    print(FCFS[c][0])
                    c +=1
            else:
                print("FCFS is empty")
            if(io):
                c = 0
                print("IO burst:")
                while c < len(io):
                    print(io[c])
                    c +=1
            else: 
                print("IO is empty")
            running[0][0] -=1
            state2 +=1
            current = 1
            Ttr +=1
      
        elif(FCFS):
            if(not running):
                running.append(FCFS.pop(b))
            if(running):
                print("Running List:")
                print(running)
            else:
                print("Running burst is empty")
            if(RR1):
                c = 0
                print("RR1 List:")
                while c < len(RR1):
                    print(RR1[c][0])
                    c +=1
            else:
                print("RR1 is empty")
            if(RR2):
                c = 0
                print("RR2 List:")
                while c < len(RR2):
                    print(RR2[c][0])
                    c +=1
            else:
                print("RR2 is empty")
            if(FCFS):
                c = 0
                print("FCFS List:")
                while c < len(FCFS):
                    print(FCFS[c][0])
                    c +=1
            else:
                print("FCFS is empty")
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
            current = 2
            
    if(io):
        IoCount(io,RR1, Ttr)
        counter(Ttr)
waiting()
average()
print(terminate)
print(Ttr)
usage = (Average.Turn/Ttr)*100

print()
print()
print()
print("MLFQ")
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
