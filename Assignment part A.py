#A 
#Take the voltage V (in volts) and resistance R (in ohms) from the user and calculate the current I = V / R.
#If the current is more than 2 A, print "Fuse will blow"; otherwise print "Circuit is safe". If R is zero or negative, print "Invalid resistance" instead.
volt=float(input('Enter Voltage'))
res=float(input('Enter resistance'))
I=volt/res
if I>2:
    print('Fuse will blow!')
elif I<=0:
    print('Invalid Resistance')
else:
    print('Circuit is Safe')

#Take a current value from the user.
#If it is positive, print "Current flows from A to B". If it is negative, print "Current flows from B to A". If it is zero, print "No current flows".
print()
I=float(input('Enter Current value'))
if I>0:
    print('Current flows from A to B')
elif I<0:
    print('Current flows from B to A')
else:
    print('No Current Flows')

#Take the colour of the first band of a resistor and print its digit:
#black = 0, brown = 1, red = 2, orange = 3, yellow = 4, green = 5, blue = 6, violet = 7, grey = 8, white = 9. For any other input print "Invalid colour". 
print()
colour = input("Enter colour: ").lower()

if colour == "black":
    print(0)
elif colour == "brown":
    print(1)
elif colour == "red":
    print(2)
elif colour == "orange":
    print(3)
elif colour == "yellow":
    print(4)
elif colour == "green":
    print(5)
elif colour == "blue":
    print(6)
elif colour == "violet":
    print(7)
elif colour == "grey":
    print(8)
elif colour == "white":
    print(9)
else:
    print("Invalid colour")

#Take two bits A and B (each 0 or 1) from the user and print the output of the AND, OR and XOR gates.
#If either input is not 0 or 1, print "Bits must be 0 or 1". Hint: AND gives 1 only when both inputs are 1. XOR gives 1 when the inputs are different.
print()
a=int(input('enter a number'))
b=int(input('enter a number'))
if (a!=0 and a!=1) or (b!=0 and b!=1):
    print('Bits must be 0 or 1 ')
else:
    A= a and b
    O= a or b
    xor= 1 if a!=b else 0
    print('And = ',A)
    print('Or = ',O)
    print('XOR = ',xor)

#Take three resistor values from the user and display the smallest and the largest of them. Use only if/ elif /else (no min() or max()).
print()
r1= float(input('enter value of R1'))
r2= float(input('enter value of R2'))
r3= float(input('enter value of R3'))
if r1>r2 and r1>r3:
    max= r1
elif r2>r1 and r2>r3:
    max= r2
else:
    max= r3
if r1<r2 and r1<r3:
    min= r1
elif r2<r1 and r2<r3:
    min= r2
else:
    min= r3
print('The max of all three resistors is',max)
print('The min of all three resistors is',min)
