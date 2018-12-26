# Imagine tha we have a car production:
cars = ['ok', 'ok', 'ok', 'error', 'ok', 'ok']

# The diffece between break and continue
# USING break
for car_status in cars:
    if car_status == 'error': # Stop the production if the 'if statement' is True
        break    # It stops the while loop        
    print(f'This car is {car_status}')
print('\n')

# USING continue
for car_status in cars:
    if car_status == 'error':
        continue # It ignores the actual loop and it goes to the next iteration
    print(f'This car is {car_status}')  # it's ignorated


for c in range(2,10):
    if c % 2 == 0: # If c is an even number
        print(f'we\'ve found an even number {c}.')
        continue  # It makes we jump to the next iteration excluding the print() bellow
    print(f'We\'ve found an odd number: {c}.')


# PRIME NUMBERS:
for n in range(2, 10):            # [2, 3, 4, 5, 6, 7, 8, 9]
    for x in range(2, number):    # O que esta dentro da lista é o x,  n= 2 [],n =3 [2], n = 4 [2,3], n = 5 [2,3,4], n = 6 [2,3,4,5], ...
        if n % x == 0:
            print(f'{n} equals {x} * {n//x}')  # (x*n)//x = n
    else:
        print(f'{n} é um número primo')



# PRIME NUMBERS BY MYSELF:

for n in range(2, 10):     # [2,3,4,5,6,7,8,9]
    for x in range(2, n):  # [], [2], [2,3], [2,3,4],...
        print(f'{n} é igual a {n}*{n//2}')  
        break
else:
    print(f'{n} é um número primo')
