
# def add_all(a1, a2, a3, a4): ao inves de fazer isso podemos fazer:
def add_all(*args):   # 'args' é a convenção para multiplos argumentos como uma tupla ou lista
    return sum(args)

def pretty_print(**kwargs):   # Recebe um dicionario e descompacta os multiplos argumentos.
    for k, v in kwargs.items():
        print(f'For {k} we have {v}.')

vals = [1, 2, 5, 7]
valsList = (1, 2, 5, 7)
vals2 = {'username':'Ricardo', 'AccesLevel':'admin'}

print(add_all(*vals))  # funciona com listas
print(add_all(*valsList)) # funciona com tuplas e qualquer iteravel que suporta o operador *(unpack)

pretty_print(**vals2)
pretty_print(**{'username':'Ricardo', 'AccesLevel':'admin'}) # Precisamos colocar o ** na frente do argumento

