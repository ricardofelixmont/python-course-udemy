# ADVANCED OPERATIONS WITH SETS
# Podemos fazer as mesmas operações matematicas com os conjuntos.

set_one = {1, 2, 3, 4, 5}
set_two = {1, 3, 5, 7, 9, 11}

# Intersecção de Conjuntos - intersection():
print(set_one.intersection(set_two))
print(set_two.intersection(set_one))
print(set_two & set_one) # atalho para intersecção

# União de Conjuntos - union() :
print(set_one.union(set_two))
print(set_two.union(set_one))
print(set_two | set_one) # atalho para união

# Diferença entre Conjuntos - difference():
# Na diferença, o resultado não é o mesmo se trocamos os conjuntos: 
print(set_one.difference(set_two))  # set_one - set_two (tudo que tem em one, mas não tem em two)
print(set_two.difference(set_one))  # set_two - set_one (tudo que tem em two, mas não tem em one)
print(set_two - set_one) # atalho para diferença

