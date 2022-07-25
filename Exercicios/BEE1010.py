# 1010 - Cálculo Simples

cod01, qPecas01, vUnit01 = input().split()
cod02, qPecas02, vUnit02 = input().split()

qPecas01 = int(qPecas01)
qPecas02 = int(qPecas02)
vUnit01 = float(vUnit01)
vUnit02 = float(vUnit02)

total = (qPecas01 * vUnit01) + (qPecas02 * vUnit02)

print("VALOR A PAGAR: R$ {:.2f}".format(total))