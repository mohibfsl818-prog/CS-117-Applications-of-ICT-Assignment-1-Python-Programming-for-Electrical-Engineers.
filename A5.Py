# SMALLEST AND LARGEST RESISTOR

R1=int(input('ENTER R1='))
R2=int(input('ENTER R2='))
R3=int(input('ENTER R3='))
# now we will apply permutation to make combination of all resistors with each other.
if R1>R2>R3:                         
    print("LARGEST=",R1,'ohm')
    print("SMALLEST=",R3,'ohm')
elif R1>R3>R2:
    print("LARGEST=",R1,'ohm')
    print("SMALLEST=",R2,'ohm')
elif R2>R1>R3:
    print("LARGEST=",R2,'ohm')
    print("SMALLEST=",R3,'ohm')
elif R2>R3>R1:
    print("LARGEST=",R2,'ohm')
    print("SMALLEST=",R1,'ohm')
elif R3>R1>R2:
    print("LARGEST=",R3,'ohm')
    print("SMALLEST=",R2,'ohm')
elif R3>R2>R1:
    print("LARGEST=",R3,'ohm')
    print("SMALLEST=",R1,'ohm')
else:
    print("EQUAL")
