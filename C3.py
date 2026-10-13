# DECIMAL TO BINARY

def decimal_to_binary(number):
    binary = ""

    while number > 0:
        digit = number % 2
        binary = str(digit) + binary
        number = number // 2

    return binary

print(decimal_to_binary(10))
print(decimal_to_binary(25))
