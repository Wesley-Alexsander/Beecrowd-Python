# 1013 - O Maior

num1, num2, num3 = input().split()
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

maiorABC = max(num1, num2, num3)

print("{} eh o maior".format(maiorABC))