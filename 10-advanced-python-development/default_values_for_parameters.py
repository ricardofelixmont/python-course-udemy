accounts = {
    'checking':1958.00,
    'savings':3695.50
}


def add_balance(amount: float, name: str = 'checking') -> float:  # Quando não passarmos o argumeno name, ele vai preencher por default com 'checking'
                                                                  # sempre que tivermos um default value, precisamos coloca-lo depois dos outros argumentos que nao tem default:
                                                                  # (amount, name = 'Ricardo') está correto, porém (name='Ricardo', amount) não está.
    """Função que recebe um valor e retorna o novo saldo."""
    accounts[name] += amount
    return accounts[name]


add_balance(500.00, 'savings')
add_balance(500.00)
print(accounts)


def create_account(name: str, holder: str, account_holders: list = []):  # O problema disso é que quando criamos a função o objeto lista é criado tambem, não é criado apenas quando chamamos a função...
    print(id(account_holders))
    account_holders.append(holder)
    return {
            'name':name, 
            'main_account_holder':holder,
            'account_holders':account_holders
}

a1 = create_account('checking', 'Rolf')
a2 = create_account('savings', 'Jen')
print(a1)
print(a2)       # Aqui vemos que a função usa a mesma default list para armazenar os dados, e vai se acumulando ao inves de zerar.




# PODEMOS RESOLVER ESSE PROBLEMA COM:
# 1. Não usando default values com 'mutable' things in python
# 2. Fazer conforme abaixo: 

def create_account(name: str, holder: str, account_holders = None):  # O problema disso é que quando criamos a função o objeto lista é criado tambem, não é criado apenas quando chamamos a função...
    if not account_holders:
        account_holders = []  # Sempre que chamarmos a função ele vai instanciar uma lista diferente.

    print(id(account_holders))
    account_holders.append(holder)
    return {
            'name':name,
            'main_account_holder':holder,
            'account_holders':account_holders
}

a1 = create_account('checking', 'Rolf')
a2 = create_account('savings', 'Jen')
print(a1)
print(a2)       # Aqui vemos que a função usa a mesma default list para armazenar os dados, e vai se acumulando ao inves de zerar.

