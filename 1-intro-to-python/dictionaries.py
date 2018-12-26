# CRIANDO DICIONARIOS
# podemos criar dicionarios de listas, de dicionarios e de tipos de dados diferenciados.
dados = [{'Lucas': {'idade':25, 'sexo':'m', 'profissao':'tecnico'}},
         {'Renata': {'idade':24, 'sexo':'f', 'profissao':'comex'}}, 
         {'Notas':(5,7,10,8,9,7)}
        ]
# dicionários são mutáveis. Podemos adicionar e remover itens.
# Podemos acessar cada elemento pelas chaves: 
item1 = dados[0]
print(item1['Lucas'])

# ou Posso fazer tudo junto:
print(dados[0]['Lucas']) # tem a mesma saída que o processo acima.

# Podemos fazer operações com os itens valor:
print(sum(dados[2]['Notas']))  # Somando os itens da tupla que esta dentro de 'Notas'
