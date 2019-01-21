from functools import wraps

user = {
        'id':1,
        'access':'admin'
        }

def third_level(access_level):
    def user_permission(func): # decorator
        @wraps(func)  # É um decorator que guarda as doc strings e o nome da função que é passada por parâmentro.
        def wrapper(panel):
            """
            Doc do wrapper...
            """
            if user.get('access') == access_level:
                return func(panel)  # aqui chamo a função para encontrar o valor.
            raise PermissionError('You\'re not admin!')
        print('Rertornando o wrapper...')
        return wrapper  # aqui passo apenas a referencia da função
    return user_permission


@third_level('admin')
def my_function(panel):
    """
    DOC da função, ele se perde quando utilizamos o decorator...
    """
    return 'Senha do admin: 1234.'


print(my_function.__name__)

print(my_function('movies'))

"""
No background do python o que acontece é o seguinte:
    user_permission = thid_level('admin')
    my_function = user_permission(my_function)
"""
