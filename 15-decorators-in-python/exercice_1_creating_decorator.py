#!/usr/bin/env python3.7
"""
1. Suponha que temos uma função 'delete_database()'
2. queremos que apenas 'user' com permissao de 'admin' possa acessá-la
3. Use o decorador 'check_permission()' e a função 'delete_database()' para criar a função 'secure_delete_database()'.
"""
user = {
    'id':1,
    'name':'jose',
    'role':'admin'
        }

def delete_database():
    print('Database deleted!')


def check_permission(func):
    def secure_delete_database():   # Normalmente se usa o nome 'wrapper' para essa função que 'embrulha' a função recebida como parãmetro.
        if user.get('role') == 'admin':
            return delete_database()
        raise PermissionError('You\'re not an admin')
    return secure_delete_database

secure_delete = check_permission(delete_database)
secure_delete()


