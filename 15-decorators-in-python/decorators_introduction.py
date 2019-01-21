#!/usr/bin/env python3.7
""" Decorators são funções de alta ordem que recebem uma first class function e retoram uma outra função modificada."""
# Como ja vimos, funções de ordem superior são funções que recebe outras funções(first class functions) como argumento.
# O que torna o decorator uma função de ordem superior diferente, é que ele precisa retornar uma função também.


# VAMOS CRIAR UM DECORATOR SIMPLES:
user = {'username': 'Ricardo', 'access_level':'admin'}
'''
def user_has_permission(func):   # este é meu decorator, ele recebe uma funcção
    
    """Esta função é um decorator, pois ele recebe e retorna uma função."""

    if user.get('access_level') == 'admin':  # O método get() é muito útil pois ele não retorna KeyError
        return func

    raise RuntimeError


def my_function():
    return "A senha do admin é 1234."

my_func = user_has_permission(my_function) # a variável 'my_func' guarda a função 'user_has_permission(my_function)'
print(my_func)  # mostra o __repr__ da funcão: <function my_function at 0x7f9cfcbf3d90> 
print(my_func()) # mostra o return da função.
'''




# Normalmente a maneira que vemos um decorator criado, tem a seguinte forma:
def user_has_permission(func):
    def secure_func():     # Criamos a função que checa se a access_level = 'admin' dentro do decorator. E ele retorna a função que passamos.
        """ Esta função não é executada, ela só é passada para o return,
            lembrando que uma função só é executada quando a chamamos."""
        if user.get('access_level') == 'admin':
            return func()
    return secure_func # Depois de checar se access_level = 'admin', ele retorna 'secure_func'.


def my_function():
    return "A senha do admin é 1234."

my_secure_function = user_has_permission(my_function)
print(my_secure_function())


# No código acima temos alguns problemas, por exemplo, podemos chamar a função 'my_function()' sem precisar passar pela secure_fuc()
# ou seja, mesmo sem ser admin podemos ter acesso a senha. 
