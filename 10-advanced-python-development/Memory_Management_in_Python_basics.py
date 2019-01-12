import sys

# Link da palestra -> https://www.youtube.com/watch?v=F6u5rhUQ6dU&feature=youtu.be

# Why should you care about memory management?
#    knowing about memory management helps you write more efficient code.


x = 300
y = 300
print(id(x))
print(id(y))


# Podemos usar o 'is' operator para comparar se x e y apontam para o mesmo objeto:
print(x is y) # -> True


# Tamanho em memoria de um dicionario e de uma tupla:
print(sys.getsizeof(dict()))
print(sys.getsizeof(tuple()))

