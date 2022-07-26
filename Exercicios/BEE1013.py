# 1013 - O Maior

"""
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:
  
  MaiorAB = (a+b+abs(a-b)) / 2

Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".
"""

num1, num2, num3 = input().split()
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

maiorABC = max(num1, num2, num3)

print("{} eh o maior".format(maiorABC))