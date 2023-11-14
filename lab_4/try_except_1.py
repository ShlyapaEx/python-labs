try:
    number1 = int(input("Введите первое число: "))
    number2 = int(input("Введите второе число: "))
    if number2 == 0:
        raise Exception("Второе число не должно быть равно 0")
    result = number1 / number2
    assert result == number1 / number2, ('Long exception chunked.')
    print("Результат деления:", result)
except ValueError:
    print("Преобразование прошло неудачно")
except ZeroDivisionError:
    print("Попытка деления числа на ноль")
except Exception as error:
    print("Общее исключение:", error)
finally:
    print("Блок try завершил выполнение")
print("Завершение программы")
