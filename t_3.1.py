while True:
    string = input("Введите список чисел через пробел: ")
    nums = []

    while len(string) != 0:
        spInd = string.find(' ')
        nums.append(string[0:spInd] if spInd != -1 else string) if string[0] != ' ' else ...
        string = string.replace(string[0:spInd+1], '', 1) if spInd != -1 else string.replace(string, '', 1)

    try:
        nums[0]
        nums = list(map(lambda num: int(num), nums))
        break
    except IndexError:
        print("Список не может быть пустым!")
    except ValueError:
        print("Список может содержать только целые числа!")


while True:
    m = input("Введите множитель (по умолчанию 2): ")

    try:
        m = int(m) if m != '' else ...
        break
    except:
        print("Множитель может быть только целым числом!")


def mult(numbers: list[int], multiplier: int = 2) -> list[int]:
    result = [num * multiplier for num in numbers]
    return result

def l_mult(numbers: list[int], multiplier: int = 2) -> list[int]:
    return list(map(lambda number: number * multiplier, numbers))


try:
    print(f"Результат (функция): {mult(nums, m)}")
    print(f"Результат (лямбда-функция): {l_mult(nums, m)}")
except:
    print(f"Результат (функция): {mult(nums)}")
    print(f"Результат (лямбда-функция): {l_mult(nums)}")