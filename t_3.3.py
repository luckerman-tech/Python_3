def function_name(search: str, status: bool, *args: tuple, **kwargs: dict) -> object:
    """
    В зависимости от значений параметров search и status либо выводит список позиционных аргументов,
    являющихся целыми числами, либо выводит строку, в которой объединены все позиционные аргументы,
    либо выводит строку, в которой выведены парами "ключ-значение" все именованные аргументы. Вызывает
    исключение в случае, если значение параметра search не равно ни "args", ни "kwargs".

    Args:
        search (str): определяет, позиционные или именованные аргументы будут обрабатываться.
        status (bool): определяет то, в каком виде будут выводиться позиционные аргументы.
        *args (tuple): позиционные аргументы.
        **kwargs (dict): именованные аргументы.
    
    Returns:
        object: список позиционных аргументов, являющихся целыми числами (list[int]),
        или строка, объединяющая в себе все позиционные аргументы (str),
        или строка, в которой выведены парами "ключ-значение" все именованные аргументы (str),
        или ничего в случае вызова исключения (None).
    
    Raises:
        ValueError: происходит в случае, если значение параметра search не равно ни "args", ни "kwargs".
    """
    result: list[int] = []
    result_2: str = ""
    if search == "args":
        if status:
            for i in args:
                if isinstance(i, int):
                    result.append(i)
            return result
        else:
            for i in args:
                result_2 += f"{i}"
            return result_2
    elif search == "kwargs":
        for k, v in kwargs.items():
            result_2 += ("Key: {}, Value: {}; ".format(k, v))
        return result_2
    else:
        raise ValueError("Error for search")
