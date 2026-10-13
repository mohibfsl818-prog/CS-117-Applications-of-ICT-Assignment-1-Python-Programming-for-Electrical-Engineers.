#RESISTORS IN SERIES

num=int(input("NUMBER OF RESISTORS: "))
total_resistance=0
for i in range(1,num+1):
    resistance=float(input(f"ENTER R{i}= "))

    total_resistance+=resistance
print("TOTAL RESISTANCE=", total_resistance)
