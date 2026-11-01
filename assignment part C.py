#C
#Write two functions: ohms_current(v, r) that returns the current I = V / R, and power_dissipated(i, r) that returns the power P = I² × R.
#Test them for V = 12 V and R = 6 ohm.
print()
def ohms_current (v,r):
    i=v/r
    print ('The current is: ',i)
def power_dissipated (i,r):
    p=(i**2)*r
    print('The power is: ',p)
v=12
r=6
i=v/r
ohms_current (v,r)
power_dissipated (i,r)

#Write a function parallel_resistance(resistors) that takes a list of resistor values and returns the equivalent resistance of the parallel combination:
#1 / R_eq = 1/R1 + 1/R2 + ...
print()

def parallel_res():
    n=int(input('Enter num of resistances'))
    total_inverse=0
    for i in range(n):
        r=int(input('value of R = '))
        total_inverse += 1/r
    Req= 1/total_inverse
    return Req
result = parallel_res()
print('Equivalent resistance ',result)

#Write a function decimal_to_binary(n) that converts a positive decimal number to a binary string using repeated division by 2 (do not use bin()). 

def decimal_to_binary(n):
    binary = ""
    
    while n > 0:
        binary += str(n % 2)
        n = n // 2
        
    return binary

num = int(input("Enter Number: "))
print(decimal_to_binary(num))

#The standard voltage divider formula assumes no current is drawn by the load,
#which is rarely true in practical circuits. Write a function loaded_divider(vs
#, r1, r2, rl) that calculates the true output voltage when a load resistor rl
#is attached in parallel with r2. The function must first compute the parallel
#equivalent of r2 and rl, then apply the voltage divider formula with vs and r1.
#Return both the unloaded theoretical voltage and the actual
#loaded voltage. Sample run: loaded_divider(12, 1000, 1000, 500) -> (6.0, 3.0)
print()
def loaded_divider(vs, r1, r2, rl):
    v_unloaded = vs * (r2 / (r1 + r2))
    r_parallel = (r2 * rl) / (r2 + rl)
    v_loaded = vs * (r_parallel / (r1 + r_parallel))
    return (v_unloaded, v_loaded)
print(loaded_divider(12, 1000, 1000, 500))

#C5. Star-Delta (Y-Δ) Transformation
print()
def s_to_d(ra, rb, rc):
    numerator = ra*rb + rb*rc + rc*ra
    r_ab = numerator / rc  
    r_bc = numerator / ra
    r_ca = numerator / rb
    return (round(r_ab, 2), round(r_bc, 2), round(r_ca, 2))
print(s_to_d(10, 20, 30))
       
