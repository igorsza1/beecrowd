from _decimal import Decimal

nota_a = Decimal(input())
nota_b = Decimal(input())
nota_c = Decimal(input())
peso1 = 2
peso2 = 3
peso3 = 5
p1 = Decimal(peso1)
p2 = Decimal(peso2)
p3 = Decimal(peso3)
MEDIA = ((nota_a * p1) + (nota_b * p2) + (nota_c * p3)) / (p1 + p2 + p3)
print(f'MEDIA = {MEDIA.__round__(1)}')