sal = float(input())

if(sal<=400.0):
    reajuste = 15
elif(sal<=800.0):
    reajuste = 12
elif(sal<=1200.0):
    reajuste = 10
elif(sal<=2000.0):
    reajuste = 7
else:
     reajuste = 4

print("Novo salario: %.2f" %(sal + (sal*reajuste/100)))
print("Reajuste ganho: %.2f" %(sal*reajuste/100))
print("Em percentual:", reajuste, "%")