#B
#A resistor has a fixed value of 10 ohm. Using a for loop, print the current through it for supply voltages from 1 V to 10 V in steps of 1 V. 
print()
r=10
for v in range (1,11,1):
    i=v/r
    print(i)
#Ask the user how many resistors are connected in series.
#Then use a loop to read the value of each resistor and print the total series resistance (R_total = R1 + R2 + ...).
n=int(input('Enter number of resistors'))
total=0
for i in range(1,n+1):
    r=float(input('enter value of r: ' ))
    total+=r
print('Req= ',total)
    
#A sensor gave these voltage readings: readings = (3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2). Using one loop (no max(), min() or sum()), find and print:
#(a) how many readings are above 3.2 V, (b) the highest reading, (c) the lowest reading, (d) the average reading
print()
readings= (3.3,3.1,3.4,2.9,3.6,3.0,3.2)
count= 0
highest= readings[0]
lowest= readings[0]
total= 0
for r in readings:
    if r>3.2:
        count += 1
    if r>highest:
        highest=r
    if r<lowest:
        lowest=r
    total += r
average = total/len(readings)
print('Readings above 3.2',count)
print('highest: ',highest)
print('lowest: ',lowest)
print('Average: ', average)

# A battery management system records voltage readings every minute. Given a hardcoded list of readings such as voltages =
#[12.6, 12.5, 12.5, 12.3, 12.1, 11.9, 12.0, 11.8, 11.6, 11.5, 11.5, 11.2], use a loop to find the longest consecutive streak of strictly decreasing
#voltage readings. Do not use built-in sorting or grouping functions. Print the length of the longest streak,
#as well as the starting and ending voltages of that specific sequence. Sample run: Longest continuous drop: 4 minutes Started at: 12.5 V Ended at: 11.9 V 
print()
voltages =[12.6, 12.5, 12.5, 12.3, 12.1, 11.9, 12.0, 11.8, 11.6, 11.5, 11.5, 11.2]
max_streak=0
max_start=0
max_end=0
current_streak=0
current_start=0
for i in range(1,len(voltages)):
    if voltages[i] < voltages[i-1]:
       if current_streak == 0:  # ye value start ko store krti hy bcz ye sign hy k streak abhi start hui
           current_start= voltages[i-1]
       current_streak+=1
       if current_streak > max_streak:
           max_streak = current_streak
           max_start = current_start
           max_end = voltages[i]
    else:
        current_streak=0
print('max streak =',max_streak+1,'minutes')
print('started at',max_start,'V')
print('ended at',max_end,'V')

# You are testing a batch of manufactured 100ohm resistors to bin them by tolerance. Write a program with a
#while loop that continuously asks the user to input a measured resistance value. The loop should stop when the user enters 0.
#Sort the inputs into three running counts: • 1% tolerance (99.0 to 101.0 ohms) • 5% tolerance (95.0 to 105.0 ohms, excluding those that qualify for 1%)
#Reject (outside 95.0 to 105.0 ohms) Print the final count of resistors in each bin once the loop terminates. 
print()
count_1=0
count_5=0
count_reject=0
value=float(input('Enter resistance values (0 to stop)'))
while value!=0:
    if value >= 99.0 and value <= 101.0 :
        count_1 += 1
    elif value >= 95.0 and value<= 105.0:
        count_5 += 1
    else:
        count_reject += 1
    value=float(input('Enter resistance values (0 to stop)'))
print('1% bin has ',count_1,' resistors')
print('5% bin has ',count_5,' resistors')
print('rejected bin have ',count_reject,' resistors')
