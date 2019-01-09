import time

def powers(limit):
    return [x**2 for x in range(limit)]


start = time.time()  # Retorna o tempo atual desde 1 de janeiro de 1970


powers(50000000)


end = time.time()

print(end - start)
