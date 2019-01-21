user = {
        'id':1,
        'access':'admin'
        }

def user_permission(func): # decorator
        
    def wrapper():
        """
        Doc do wrapper...
        """
        if user.get('access') == 'admin':
            return func()  # aqui chamo a função para encontrar o valor.
        raise PermissionError('You\'re not admin!')
    print('Rertornando o wrapper...')
    return wrapper  # aqui passo apenas a referencia da função


@user_permission
def my_function():
    """
    DOC da função, ele se perde quando utilizamos o decorator...
    """
    return 'Senha do admin: 1234.'

print(my_function())
print(my_function.__name__)
print(my_function.__doc__)

