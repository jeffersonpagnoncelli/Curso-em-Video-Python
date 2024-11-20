import math
num = float(input('Digite um numero decimal: '))
num_novo = math.floor(num)
print(num_novo)

from math import sin,cos,tan,hypot
cateto1 = float(input('Digite o valor do primeiro cateto: '))
cateto2 = float(input('Digite o valor do segundo cateto: '))
hip = hypot(cateto1, cateto2)
print(hip)

from math import sin,cos,tan,radians
angulo = float(input('Digite o valor do angulo que deseja calcular: '))
sen = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))
print('O valor escolhido do angulo é {} o seno é {:.2f} o cosseno é {:.2f} e a tangente é {:.2f}'.format(angulo, sen, cos, tan))