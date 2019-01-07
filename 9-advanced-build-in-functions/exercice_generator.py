#!/usr/bin/env python3.7

# Prime numbers: 

def prime_numbers(bound):
    for n in range(2, bound):
        for x in range(2,n):  # [],[2],[2,3],[2,3,4],...
            if n % x == 0:
                # Não é um número primo
                break
        else:
            yield n

x = prime_numbers(20)
print(x)  # Mostra o __repr__ do objeto generator

# Posso iterar sobre esse objeto com a função next
print(next(x))
print(next(x))
print(next(x))

# Também posso iterar sobre um generator com os laços:
y = prime_numbers(20)

for prime in y:
    print(prime)


