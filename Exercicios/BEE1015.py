# 1015 - Distância Entre Dois Pontos

import math

x1, y1 = input().split()
x2, y2 = input().split()

x1 = float(x1)
x2= float(x2)
y1 = float(y1)
y2= float(y2)

firstCoordinate = (x2 - x1) ** 2
secondCoordinate = (y2 - y1) ** 2

answer = math.sqrt(firstCoordinate + secondCoordinate)

print(f"{answer:.4f}")
