# CONTINUOUS DISCHARGE ANALYSIS

voltages = [12.6, 12.5, 12.5, 12.3, 12.1, 11.9, 12.0, 11.8, 11.6, 11.5, 11.5, 11.2]

count = longest = 1
start = temp = end = voltages[0]

for i in range(1, len(voltages)):
    if voltages[i] < voltages[i-1]:
        count += 1
        if count > longest:
            longest = count
            start = temp
            end = voltages[i]
    else:
        count = 1
        temp = voltages[i]

print("LONGEST CONTINUOUS DROP:", longest, "minutes")
print("STARTED AT:", start, "V")
print("ENDED AT:", end, "V")
