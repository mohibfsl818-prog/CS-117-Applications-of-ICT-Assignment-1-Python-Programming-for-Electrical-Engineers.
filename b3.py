# Sensor Readings

voltage=[3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2]
count=0
total=0
high=voltage[0]
low=voltage[0]
for i in voltage:
    if i>3.2:
        count+=1

    if i > high:
        high=i

    if i < low:
        low=i

    total=total+i

avg=total/7
print("READING ABOVE 3.2V=",count)
print("HIGHEST=",high,"V")
print("LOWEST=",low,"V")
print("AVG=",avg)
