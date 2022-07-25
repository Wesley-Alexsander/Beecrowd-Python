# 1009 - Salário com Bônus

vendedor = input()
salario = float(input())
vendas = float(input())

comissao = vendas * 0.15 
salario += comissao

print("TOTAL = R$ %0.2f" %salario)