import typing
def repeated_function(aString: str, n: int) -> str:
    if n == 1:
        return aString
    else:
        return aString + repeated_function(aString, n-1)

print(repeated_function("Nome", 3))

