# Current and Power

def ohms_current(v, r):
    return v / r

def power_dissipated(i, r):
    return i * i * r

current = ohms_current(12, 6)
power = power_dissipated(current, 6)

print("CURRENT=", current,"A")
print("POWER=", power,"W")
