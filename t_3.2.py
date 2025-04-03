def plus():
    a = input("Слагаемое 1: ")
    try:
        a = float(a)
    except:
        ...
    if isinstance(a, str):
        raise ValueError("Слагаемое должно быть числом!")

    b = input("Слагаемое 2: ")
    try:
        b = float(b)
    except:
        ...
    if isinstance(b, str):
        raise ValueError("Слагаемое должно быть числом!")

    res = a + b

    if (res == round(res)):
        res = int(res)
    return f">>> {res}\n-------------------------"


def minus():
    a = input("Уменьшаемое: ")
    try:
        a = float(a)
    except:
        ...
    if isinstance(a, str):
        raise ValueError("Уменьшаемое должно быть числом!")

    b = input("Вычитаемое: ")
    try:
        b = float(b)
    except:
        ...
    if isinstance(b, str):
        raise ValueError("Вычитаемое должно быть числом!")

    res = a - b

    if (res == round(res)):
        res = int(res)
    return f">>> {res}\n-------------------------"


def mult():
    a = input("Множитель 1: ")
    try:
        a = float(a)
    except:
        ...
    if isinstance(a, str):
        raise ValueError("Множитель должен быть числом!")

    b = input("Множитель 2: ")
    try:
        b = float(b)
    except:
        ...
    if isinstance(b, str):
        raise ValueError("Множитель должен быть числом!")

    res = a * b

    if (res == round(res)):
        res = int(res)
    return f">>> {res}\n-------------------------"


def division():
    print("Виды деления:\n1. Обычное деление\n2. Остаток от деления\n3. Деление нацело")
    option = input("Выберите вид деления (цифра от 1 до 3 включительно): ")
    if option not in ['1', '2', '3']: raise ValueError("Неизвестное значение!")

    a = input("Делимое: ")
    try:
        a = float(a)
    except:
        ...
    if isinstance(a, str):
        raise ValueError("Делимое должно быть числом!")

    b = input("Делитель: ")
    try:
        b = float(b)
    except:
        ...
    if isinstance(b, str):
        raise ValueError("Делитель должен быть числом!")
    elif b == 0:
        raise ZeroDivisionError("Делить на ноль нельзя!")

    if option == '1':
        res = a / b
    elif option == '2':
        res = a % b
    else:
        res = a // b

    if (res == round(res)):
        res = int(res)
    return f">>> {res}\n-------------------------"


def power():
    a = input("Основание: ")
    try:
        a = float(a)
    except:
        ...
    if isinstance(a, str):
        raise ValueError("Основание должно быть числом!")

    b = input("Показатель: ")
    try:
        b = float(b)
    except:
        ...
    if isinstance(b, str):
        raise ValueError("Показатель должен быть числом!")

    res = a ** b

    if not isinstance(res, complex):
        if res == round(res):
            res = int(res)
    return f">>> {res}\n-------------------------"


def fact():
    a = input("Число: ")
    try:
        a = int(a)
    except:
        ...
    if isinstance(a, str) or a < 0:
        raise ValueError("Должно быть введено целое неотрицательное число!")
    
    res = 1
    for i in range(1, a+1):
        res *= i
    
    return f">>> {res}\n-------------------------"


def mean():
    string = input("Список чисел: ")
    nums = []

    while len(string) != 0:
        index = string.find(' ')
        nums.append(string[0:index] if index != -1 else string) if string[0] != ' ' else ...
        string = string.replace(string[0:index+1], '', 1) if index != -1 else string.replace(string, '', 1)
    
    try:
        nums[0]
        nums = list(map(lambda num: float(num), nums))
    except IndexError:
        raise ValueError("Список не может быть пустым!")
    except ValueError:
        raise ValueError("Список может содержать только числа!")
    
    sum = 0
    for num in nums:
        sum += num
    res = sum / len(nums)

    if (res == round(res)):
        res = int(res)
    return f">>> {res}\n-------------------------"


def sqrt():
    a = input("Число, из которого извлекается квадратный корень: ")
    try:
        a = float(a)
    except:
        ...
    if isinstance(a, str) or a < 0:
        raise ValueError("Должно быть введено неотрицательное число!")
    
    res = a ** 0.5

    if (res == round(res)):
        res = int(res)
    return f">>> {res}\n-------------------------"


def choice(ch):
    if ch == '1':
        print(plus())
    elif ch == '2':
        print(minus())
    elif ch == '3':
        print(mult())
    elif ch == '4':
        print(division())
    elif ch == '5':
        print(power())
    elif ch == '6':
        print(fact())
    elif ch == '7':
        print(mean())
    elif ch == '8':
        print(sqrt())
    else:
        raise ValueError("Неизвестная операция!")

while True:
    print("Доступные операции:\n1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление\n5. Возведение в степень\n6. Факториал\n7. Среднее арифметическое\n8. Квадратный корень\nexit (Завершение работы)\n-------------------------")
    op = input("Операция: ")
    if op == "exit":
        break
    choice(op)
    input("Введите любую строку для продолжения ")
    print("\n")