class FixedFloat:
    def __init__(self, amount):
        """Método de instância"""
        self.amount = amount

    def __repr__(self):
        """Método de instância"""
        return f'<fixedFloat {self.amount:.2f}>'
    
    def from_sum(self, value1, value2):
        """ Digamos que queremos um metodo que retorna um objeto do tipo 
            FixedFloat.
        """
        return FixedFloat(value1 + value2)


    @staticmethod
    def from_multiple(value1, value2):
        return FixedFloat(value1 * value2) # FixedFloat formata o resultado

    @classmethod
    def from_div(cls, value1, value2):
        return cls(value1 / value2) # Substituimos FixedFloat pelo 'cls' que é
                                    # a classe que foi passada como argumento.

number = FixedFloat(18.5746) # Instanciamos um novo objeto do tipo FixedFloat
print(number) # mostra o retorno do método de instância '__repr__'

# Aqui criamos um objeto FixedFloat a partir do retorno do método Fixedfloat
""" Porém não é interessante fazer isso, pois precisamos criar uma instancia da
    classe(que nunca iremos utilizar, que no caso é 'number') para podermos 
    invocar o método 'from_sum'.
"""
new_number = number.from_sum(19.575, 0.789)
print(new_number)


# Para podermos utilizar o método 'from_sum' sem precisar instanciar 
# a classe, utilizamos @staticmethod como no método 'from_multiple'
# Então:
new_number2 = FixedFloat.from_multiple(2, 4)
print(new_number2)



# OUTRO EXEMPLO:
# digamos que temos uma classe Euro, que herda de FixedFloat
class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = '$'
        
    def __repr__(self):
        return f'<Euro {self.symbol}{self.amount:.2f}>'

# Agora vamos chamar o método 'from_multiple' a partir da classe 'Euro'
money = Euro.from_multiple(16.758, 9.999)
print(money) 
""" Vamos ter a seguinte mensagem: <fixedFloat 167.56> 
    é um objeto do tipo FixedFloat, isso esta errado! Queremos um objeto do 
    tipo Euro.
    Podemos resolver esse 'bug' com o decorador @classmethod(que tem a classe
    como parametro.
    Fiz isso como exemplo no método 'from_div()
"""
dinheiro = Euro.from_div(16, 2)
print(dinheiro) # <Euro $8.00>


# CONSIDERAÇÕES IMPORTANTES:
############################
""" Muitos na comunidade Python são contra os @staticmethods
    eles dizem: "@staticmethod é um @classmethod com menos funcionalidades
    e sem beneficios. 

    A recomendação é utilizar @classmethod sempre que você não precisar do
    'self'
"""
############################ 

# Usamos métodos estaticos quando temos certeza de que não queremos herdar
# aquele método.


# EXERCICIO MOSTRANDO UM BOM USO DE @staticmethod
"""There are some cases where we don't need to use self  in a method. For example, the greet_friend()  method below:"""
class Person:
    def __init__(self, name):
        self.name = name

    def greet_friend(self, friend_name):
        return f'Hey there, {friend_name}!'

"""Which would be a better alternative, @classmethod  or @staticmethod ? Before answering, think carefully about why."""

# Resposta: @staticmethod
# That's correct! Because we don't need access to either self or cls
# (which @classmethod gives us), we could just use @staticmethod instead.

