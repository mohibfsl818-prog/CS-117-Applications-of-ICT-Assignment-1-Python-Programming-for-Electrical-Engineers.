# OHM'S LAW TABLE

resistance=10
voltage=1
for i in range(1,11):
    current=voltage/resistance
    print('VOLTAGE=',voltage,"V",";",'CURRENT=',current,'amp')
    voltage += 1
