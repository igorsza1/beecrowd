# 1024 - Criptografia

## [Descrição](https://www.beecrowd.com.br/judge/pt/problems/view/1024)

## Solução

### Python 3.11

```python
N = int(input())

for _ in range(N):
    M = input()

    novoM = ""
    for letra in M:
        novoM += chr(ord(letra) + 3) if letra.isalpha() else letra
    M = novoM[::-1]
    M = M[:len(M)//2] + ''.join([chr(ord(letra) - 1) for letra in M[len(M)//2:]])

    print(M)
```
