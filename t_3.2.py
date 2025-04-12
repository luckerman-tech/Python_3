def data_entering(prompt: str, e: str):
    num = input(prompt)
    try:
        num = float(num)
    except:
        False
    if isinstance(num, str):
        raise ValueError(e)
    return num


def res_processing(result):
    if (result == round(result)):
        result = int(result)
    return f">>> {result}\n-------------------------"


def plus():
    a = data_entering("Слагаемое 1: ", "Слагаемое должно быть числом!")
    b = data_entering("Слагаемое 2: ", "Слагаемое должно быть числом!")

    res = a + b
    return res_processing(res)


def minus():
    a = data_entering("Уменьшаемое: ", "Уменьшаемое должно быть числом!")
    b = data_entering("Вычитаемое: ", "Вычитаемое должно быть числом!")

    res = a - b
    return res_processing(res)


def mult():
    a = data_entering("Множитель 1: ", "Множитель должен быть числом!")
    b = data_entering("Множитель 2: ", "Множитель должен быть числом!")

    res = a * b
    return res_processing(res)


def division():
    print("Виды деления:\n1. Обычное деление\n2. Остаток от деления\n3. Деление нацело")
    option = input("Выберите вид деления (цифра от 1 до 3 включительно): ")
    if option not in ['1', '2', '3']: raise ValueError("Неизвестное значение!")

    a = data_entering("Делимое: ", "Делимое должно быть числом!")
    b = data_entering("Делитель: ", "Делитель должен быть числом!")
    if b == 0:
        raise ZeroDivisionError("Делить на ноль нельзя!")

    if option == '1':
        res = a / b
    elif option == '2':
        res = a % b
    else:
        res = a // b

    return res_processing(res)


def power():
    a = data_entering("Основание: ", "Основание должно быть числом!")
    b = data_entering("Показатель: ", "Показатель должен быть числом!")

    res = a ** b
    if not isinstance(res, complex):
        return res_processing(res)
    return f">>> {res}\n-------------------------"


def fact():
    a = input("Число: ")
    try:
        a = int(a)
    except:
        False
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
        nums.append(string[0:index] if index != -1 else string) if string[0] != ' ' else False
        string = string.replace(string[0:index+1], '', 1) if index != -1 else string.replace(string, '', 1)
    
    try:
        nums = list(map(lambda num: float(num), nums))
    except ValueError:
        raise ValueError("Список может содержать только числа!")
    if not(nums):
        raise ValueError("Список не может быть пустым!")
    
    sum = 0
    for num in nums:
        sum += num
    res = sum / len(nums)

    return res_processing(res)


def sqrt():
    a = data_entering("Число, из которого извлекается квадратный корень: ", "Должно быть введено неотрицательное число!")
    if a < 0:
        raise ValueError("Должно быть введено неотрицательное число!")
    
    res = a ** 0.5
    return res_processing(res)


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
