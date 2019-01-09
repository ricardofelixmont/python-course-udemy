# objetos que gerenciam data and time e não se preocupam com timezones são chamados de 'naive' em python.

# Por exemplo: 
from datetime import datetime
print(datetime.now())   # Pega o horário corrente do seu computador.
# Não são muito úteis pois quando queremos armazenar esse dados em um banco de dados ou um arquivo, ele vai trazer as datas de varias pessoas 
# sem nenhuma referencia. Não sambemos se aquele horario é do Brazil ou da Alemanha por exemplo.


# objetos que gerenciam date and time e se preocupam com timezones são chamados de 'aware' em python.
from datetime import timezone
print(datetime.now(timezone.utc))   # UTC é a referencia a que todos os paises do mundo se referem a data.




""" O módulo principal de data e time do python é o: datatime
    e uma das classes mais importantes desse módulo é confusamente a datetime"""

from datetime import datetime, timezone, timedelta

print(datetime.now()) # é um 'naive' pois não retorna nenhuma informação sobre 'timezones', o método now() retorna o current time do computador 
""" Um problema do datime é que ele nao mostra a hora baseado nos timezones, então não temos como mostrar o datetime.now() para um usuário 
    pois não sabemos se esse é o horário certo para ele."""

# Porém podemos informar para o now() o timezone.

print(datetime.now(timezone.utc))   # UTC é o timezone universal padrão.
                                    # Por exemplo, alguem no Brazil e outra pessoa no Japão falando em UTC, ambos estão falando sobre o mesmo horário.
""" O melhor é sempre usar UTC como padrão para os nossos programas pois se estivermos em qualquer lugar do mundo podemos
    converter o horário pois o offset é zero. Por exemplo datetime.now(timezone.utc) retorna (2019-01-09 15:09:16.052850+00:00)
    e a partir dai conseguimos fazer a conversão com facilidade para qualquer timezone."""



# timedelta: trabalha a diferença de horarios
""" timdelta é bem útil para fazer conversões de date and time.
    PODE RECEBER COMO PARAMETROS:
        class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0) """

today = datetime.now(timezone.utc)
tomorrow = today + timedelta(days=1)
print(tomorrow)


# Formatando data and time:
print(today.strftime('%d-%m-%Y %H:%M:%S'))   # strftime = string format time

user_date = input('Enter the date in YYYY-mm-dd format: ')
user_date = datetime.strptime(user_date, '%Y-%m-%d')    # strptime = string parse time
print(user_date)    # Aqui também não temos timezone, ou seja, 'naive'

