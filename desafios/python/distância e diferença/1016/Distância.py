codigo1, quant1, valor1 = input().split()
codigo1, quant1, valor1 = int(codigo1), int(quant1), float(valor1)
codigo2, quant2, valor2 = input().split()
codigo2, quant2, valor2 = int(codigo2), int(quant2), float(valor2)

total = (quant1 * valor1) + (quant2 * valor2)
print(f"VALOR A PAGAR: R$ {total:.2f}")