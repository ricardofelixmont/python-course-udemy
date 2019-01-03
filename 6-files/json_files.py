# JSON (JavaScript Object Notation)
# o formato Json veio do java, é uma notação de objeto em Java. É um dos formatos de arquivo mais populares do mundo.
# se não o maior.

# DIFERENÇAS ENTRE JSON FILES E DICIONARIOS:
# Apesar de ter a mesma notaçao de um dicionario no python.
# 1. O json file é uma string. É armazenado em um arquivo de texto.
# 2. O json file sempre usa aspas duplas "" e nunca aspas simples.

# EXEMPLO DE JSON FILE:
# abaixo segue o padrão do arquivo json...
{
    "friends":[
        {
            "name":"Jose",
            "Curso":"Engenharia"
        },
        {
            "name":"Rold",
            "curso":"Ciencia da Computação"
        },
        {
            "name":"Anna",
            "curso":"Computação"
        }
    ]
}

# alguns programas aceitam a seguinte notação para arquivos json, mas não é recomendado fazer:
# utiliza colchetes ao invés de chaves.
[
    "friends":[
        {
            "name":"Jose",
            "Curso":"Engenharia"
        },
        {
            "name":"Rold",
            "curso":"Ciencia da Computação"
        }
        {
            "name":"Anna",
            "curso":"Computação"
        }
    ]
]

""" Se esquecermos da virgula por exemplo, os dicionarios dentro da lista podemos nos deparar com o seguinte erro:

    Traceback (most recent call last):
  File "reading_json_files.py", line 4, in <module>
    data = json.load(f)
  File "/home/semantix/anaconda3/lib/python3.7/json/__init__.py", line 296, in load
    parse_constant=parse_constant, object_pairs_hook=object_pairs_hook, **kw)
  File "/home/semantix/anaconda3/lib/python3.7/json/__init__.py", line 348, in loads
    return _default_decoder.decode(s)
  File "/home/semantix/anaconda3/lib/python3.7/json/decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "/home/semantix/anaconda3/lib/python3.7/json/decoder.py", line 353, in raw_decode
    obj, end = self.scan_once(s, idx)
json.decoder.JSONDecodeError: Expecting ',' delimiter: line 11 column 9 (char 198)


""""
