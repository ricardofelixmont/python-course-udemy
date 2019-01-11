""" Regex não é uma linguagem de programação, porém é uma linguagem de 
busca de padrões."""

"""
Os quatro componentes mais importantes do Regex, são usados o tempo todo:

    (.) Ponto significa qualquer coisa, qualquer caracter, exceto newlines(\n).
    (+) One or more of.
    (*) Zero or more of.
    (?) Zero or one of.

    (\) siginifica literal, por exemplo se quiser digitar o (.) como sendo algo que queremos encontrar, podemos fazer \.

jose@tecladocode.com

-> para selecionar a linha acima podemos fazer: .*  
# Podemos testar nosso código no regex101.com    


# O curso nao ensinou muita coisa sobre regex, apenas um pequeno overview.
# Link de uma boa leitura de referencia: 
    https://medium.com/trainingcenter/entendendo-de-uma-vez-por-todas-express%C3%B5es-regulares-parte-5-5ffd39138f2

"""

# Exercício:
"""
1. The file name must start with an English letter or a number(a-zA-Z0-9).
2. The file name can only contain English letters, numbers and symbols among these four: _-()
3. The file name must end with proper file extension among .jpg, .jpeg, .png, .gif
"""

import re
 
 
def is_filename_safe(filename):
    """ This function user regex to identify whether a file is safe or not, based on the three concepts above."""
    regex = '^[a-zA-Z0-9][a-zA-Z0-9_()-]*(\.jpg|\.jpeg|\.png|\.gif)$'
    # ^[a-zA-Z0-9]      start with a-zA-Z0-9
    # [a-zA-Z0-9_()-]+      then only contains a-zA-Z0-9_()- for any number of times
    # (\.jpg|\.jpeg|\.png|\.gif)$       at last, it must end with one of the four extensions, remember to escape the dot
    # since we check from start to end, it can either match the whole string or none
    return re.match(regex, filename) is not None

print(is_filename_safe('ricardo.jpg'))
