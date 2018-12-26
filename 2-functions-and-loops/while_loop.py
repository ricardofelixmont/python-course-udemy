is_programmer = False

# It's a infinite loop
while not(is_programmer): # It means that: is_programmer == True 
    print('Leraning Programming')
    learning_programming = input('Are you alredy a programmer? ').lower()
    is_programmer = learning_programming == 'yes' # is_programmer receives the boolean value of following comparision

# We can use while loop to repeat something a specific number os times:
i = 0   # control variable
while i < 10:
    print('{}° repetition'.format(i+1))
    i += 1  # Here we have to increment the control variable

# We can also use while loops to control some variable like temperature:
temperature = 15
while temperature < 20:
    print('Heating...')
    temperature += 1

