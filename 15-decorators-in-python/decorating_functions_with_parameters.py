from functools import wraps

user = {
        'id':1,
        'access':'admin'
        }

def user_permission(func): # decorator
    @wraps(func)  # É um decorator que guarda as doc strings e o nome da função que é passada por parâmentro. 
    def wrapper(panel = 'Movies'):  # Se eu colocar como padrão para a função, eu torno o
        """
        Doc do wrapper...
        """
        if user.get('access') == 'admin':
            return func(panel)  # aqui chamo a função para encontrar o valor.
        raise PermissionError('You\'re not admin!')
    print('Rertornando o wrapper...')
    return wrapper  # aqui passo apenas a referencia da função



@user_permission
def my_function(panel): # Agora colocamos um parametro para essa função.
    """
    DOC da função, ele se perde quando utilizamos o decorator...
    """
    return f'Senha do admin:{panel} 1234.'


print(my_function())
print(my_function('Filmes'))
print(my_function.__name__)
print(my_function.__doc__)

