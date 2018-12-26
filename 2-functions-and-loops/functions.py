# Funçoes:
# Funçoes podem ser definidas em qualquer ordem porém só podem

def check_if_prime(number):   # 'number' é chamada de PARAMETRO
    for x in range(2, number):
        if number % x == 0:
            print(number, 'equals', x, '*', number//x)
            break
    else:
        print(number, 'is a prime number')

def check_primes(limite):
    for n in range(2,limite):
        check_if_prime(n) # 'n' é chamada de ARGUMENTO


limite = int(input('Digite um limite: '))
check_primes(limite)

# Não é interessante usar variaveis de fora do bloco:
x = 10

def bloco():
    # x += 1 isso da erro pois nao podemos atribuir valores a variaveis fora do bloco
    # Podemos apenas acessa-los
    y = x + 10
    return y   # return termina a função, returna um valor e nao uma variavel. As variaveis só existe dentro do bloco
    print(y) # não vai ser impresso
print(bloco())

