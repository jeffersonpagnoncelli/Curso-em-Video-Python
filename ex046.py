import time
start = str(input('Para começar a queima de fogos digite "INICIAR": \n'))
for c in range(10, -1, -1):
    time.sleep(1)
    print(c)
print('BOOOOOOOM!')