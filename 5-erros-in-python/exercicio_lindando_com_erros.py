def power_of_two():
    user_input = input('Please enter a number: ')
    try:
        n = float(user_input)
    except ValueError:
        print('Your input was invalid. Using default value 0')
        return 0
    finally:
        n_square = n ** 2
        # o correto é colocar tudo que queremos fazer dentro do bloco try
        return n_square


print(power_of_two())


# MANEIRA CORRETA DE FAZER O TRY EXCEPT ACIMA:
def power_of_three():
    user_input = input('Please enter a number: ')
    try:
        n = float(user_input)
        n_square = n ** 3
        return n_square
    except:
        print('Your input was invalid. Using default as 0.')
        return 0

print(power_of_three())
