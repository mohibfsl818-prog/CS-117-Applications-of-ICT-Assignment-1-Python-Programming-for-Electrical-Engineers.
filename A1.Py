# FUSE CHECK (OHM'S LAW)

voltage=int(input("VOLTAGE(Volt)="))
resistance=int(input("RESISTANCE(ohm)="))
if resistance>0:
    current = voltage / resistance
    print("CURRENT(amp)=",current)
    if current>2:
        print("FUSE WILL BLOW")
    else:
        print("CIRCUIT IS SAFE")
if resistance==0 or resistance<1:
    print("INVALID RESISTANCE")
