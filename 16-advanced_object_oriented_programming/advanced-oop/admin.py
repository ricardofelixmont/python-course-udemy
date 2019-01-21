from user import User
from database import Database
from saveable import Saveable


class Admin(User, Saveable):
    def __init__(self, username, password, access):
        super().__init__(username, password)
        self.access = access

    def __repr__(self):
        return f'<Admin {self.username}, access {self.access}>'

    def to_dict(self):
        return {
            'username':self.username,
            'password':self.password,
            'access':self.access
        }

    def save(self):
        Database.insert(self.to_dict())


if __name__=='__main__':
    admin = Admin('Ricardo', '123', 'Usuario')
    print(admin.username)
    print(admin.password)
    print(admin)
    

