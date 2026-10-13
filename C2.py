# PARALLEL RESISTANCE

def parallel_resistance(resistors):
    sum = 0

    for resistor in resistors:
        sum = sum + (1 / resistor)

    equivalent = 1 / sum

    return round(equivalent, 2)

print(parallel_resistance([10, 10]))
print(parallel_resistance([100, 200, 300]))
