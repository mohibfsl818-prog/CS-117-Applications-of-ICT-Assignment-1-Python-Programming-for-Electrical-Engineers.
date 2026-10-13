# LOGIC GATES

bit_1=int(input('Enter A= '))
bit_2=int(input('Enter B= '))

if bit_1==1 and bit_2==1:
    print('AND=1')
    print('OR=1')
    print('XOR=0')
elif bit_1==1 and bit_2==0:
    print('AND=0')
    print('OR=1')
    print('XOR=1')
elif bit_1==0 and bit_2==1:
    print('AND=0')
    print('OR=1')
    print('XOR=1')
elif bit_1==0 and bit_2==0:
    print('AND=0')
    print('OR=0')
    print('XOR=0')
else:
    print('BITS MUST BE 0 OR 1')
