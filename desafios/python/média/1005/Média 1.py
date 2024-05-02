from _decimal import Decimal

nota1 = Decimal(input())
nota2 = Decimal(input())
peso1 = 3.5
peso2 = 7.5
p1 = Decimal(peso1)
p2 = Decimal(peso2)
media = ((nota1 * p1) + (nota2 * p2)) / (p1 + p2)
print(f'MEDIA = {media.__round__(5)}')