class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        return 'logged in!'

    def __repr__(self):
        return f'<User {self.username}>'
     



if __name__=='__main__':
    usuario_teste = User('Ricardo', '123')
    print(f'Usuário: {usuario_teste.username}')
    print(f'Senha: {usuario_teste.password}')
    print(usuario_teste)
