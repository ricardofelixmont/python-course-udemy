#!/usr/bin/env python3.7
# Lets suppose that we want to create a list from zero to a hundred

def hundred():
    lista = list()
    count = 0
    while count < 100:
        lista.append(count)
        count += 1 
    return lista

print(hundred())


''' No exemplo acima criamos uma lista pequena que não tem muito impacto na memoria. Porém se quisermos fazer
    uma lista que possua um milhão de números, isso pode ser um pouco prejudicial em performance.'''

def million():
    lista = []
    count = 0
    while count < 1000000:
        lista.append(count)
        count += 1
    return lista

# listas = million()
# Isso ja demora um pouco mais e consome mais memoria.
# print(listas)



def numbers():   # Generator
    for c in range(0,100):
        yield c


x = numbers()   # x é um iterator
print(x)
# A função next faz com que o generator seja executado até o 'yield statement'
print(next(x))
# Um generator lembra o estado anterior(numero anterior) para que quando chamarmos next()  
print(next(x))

# Podemos iterar sobre o Generator:
for c in x:
    print(c,end='->')


# Como posso iterar sobre essas funções, eles são generator, iterators e também são iterables.
