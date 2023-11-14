class NegValException(Exception):
    pass


# Пример использования пользовательского исключения NegValException
try:
    val = int(input("input positive number: "))
    if val < 0:
        raise NegValException("Neg val: " + str(val))
    print(val + 10)
except NegValException as error:
    print(error)
