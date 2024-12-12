def trig_test(x, function_type):
    """
    Вычисляет значение тригонометрической функции для заданного угла.

    :param x: Угол в градусах.
    :type x: float
    :param function_type: Тип тригонометрической функции ('sin', 'cos', 'tg', 'ctg').
    :type function_type: str
    :returns: Значение тригонометрической функции.
    :rtype: float
    :raises ZeroDivisionError: Если тангенс или котангенс не определены.
    :raises ValueError: Если указан неизвестный тип тригонометрической функции.
    """
    x = x / 180 * 3.1415
    q = x
    s = 0
    for i in range(1, 1000):
        s += q
        q = q * (-1) * (x * x) / ((2 * i + 1) * (2 * i))
    try:
        if function_type == "sin":
            return round(s, 3)
        g = round(s, 3)
        cos_x = (1 - g**2) ** 0.5
        if function_type == "cos":
            return round(cos_x, 3)
        if function_type == "tg":
            if cos_x == 0:
                raise ZeroDivisionError("Тангенс не определён для данного угла.")
            return round(g / cos_x, 3)
        if function_type == "ctg":
            if g == 0:
                raise ZeroDivisionError("Котангенс не определён для данного угла.")
            return round(cos_x / g, 3)
        raise ValueError("Неизвестный тип тригонометрической функции.")
    except ZeroDivisionError as e:
        return str(e)
    except ValueError as e:
        return str(e)

def convert_test(num, base):
    """
    Преобразует число в строку, представляющую его в заданной системе счисления.

    :param num: Число для преобразования.
    :type num: int
    :param base: Основание системы счисления (от 2 до 36).
    :type base: int
    :returns: Строка, представляющая число в заданной системе счисления.
    :rtype: str
    :raises ValueError: Если основание системы счисления не в диапазоне от 2 до 36.
    """
    if base < 2 or base > 36:
        raise ValueError("Основание системы счисления должно быть в диапазоне от 2 до 36.")
    if num < 0:
        return '-' + convert_test(-num, base)
    elif num == 0:
        return '0'
    digits = []
    while num:
        digits.append(int(num % base))
        num = num // base
    if base > 10:
        for i in range(len(digits)):
            if digits[i] >= 10:
                digits[i] = chr(digits[i] - 10 + ord('A'))
    return ''.join(str(x) for x in digits[::-1])

def factorial_test(x):
    """
    Вычисляет факториал заданного неотрицательного целого числа.

    :param x: Целое неотрицательное число, для которого нужно вычислить факториал.
    :type x: int
    :returns: Факториал числа x.
    :rtype: int
    :raises ValueError: Если x не является неотрицательным целым числом.
    """
    if not isinstance(x, int):
        raise ValueError
    if x < 0:
        raise ValueError
    result_fact = 1
    for h in range(2, x + 1):
        result_fact *= h
    return result_fact

def evaluate_expression_test(expression):
    """
    Оценивает арифметическое выражение и возвращает результат.

    :param expression: Арифметическое выражение в виде строки.
    :type expression: str
    :returns: Результат вычисления выражения.
    :rtype: float
    :raises ZeroDivisionError: Если в выражении происходит деление на ноль.
    """
    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Данное выражение не определено"

def process_key(key, entry_text, abs_value=0):
    """
    Обрабатывает нажатие клавиши и возвращает новый текст для ввода.

    :param key: Нажатая клавиша.
    :type key: str
    :param entry_text: Текущий текст в поле ввода.
    :type entry_text: str
    :param abs_value: Абсолютное значение (по умолчанию 0).
    :type abs_value: float
    :returns: Новый текст для ввода и абсолютное значение.
    :rtype: tuple
    """
    try:
        if key == "=":
            str_1 = "0123456789*)(/."
            if not entry_text or entry_text[0] not in str_1:
                return "Ошибка: неверный ввод", abs_value
            result = evaluate_expression_test(entry_text)
            if isinstance(result, str):
                return "Данное выражение не определено", abs_value
            return str(result), result
        elif key == "Del":
            return "", abs_value
        elif key == "±":
            if not entry_text:
                return "-", abs_value
            return entry_text[1:] if entry_text[0] == "-" else "-" + entry_text, abs_value
        elif key == "Abs":
            return str(abs_value), abs_value
        elif key in ["sin", "cos", "tg", "ctg"]:
            return str(trig_test(float(entry_text), key)), abs_value
        elif key == "x!":
            return str(factorial_test(int(entry_text))), abs_value
        elif key in ["+", "-", "*", "/", ")", "("]:
            return entry_text + key, abs_value
        elif key in ["2-ная", "3-ная", "4-ная", "5-ная", "6-ная", "7-ная", "8-ная", "9-ная", "16-ная"]:
            base = int(key.split('-')[0])
            return str(convert_test(int(entry_text), base)), abs_value
        elif key == "xⁿ":
            return entry_text + "**", abs_value
        else:
            return entry_text + key, abs_value
    except Exception as e:
        return f"Ошибка: {str(e)}", abs_value

def calc(key):
    """
    Обрабатывает нажатие клавиши калькулятора и обновляет текст в поле ввода.

    :param key: Нажатая клавиша.
    :type key: str
    """
    global Abs
    entry_text = calc_entry.get()
    new_text, Abs = process_key(key, entry_text, Abs)
    calc_entry.delete(0, END)
    calc_entry.insert(END, new_text)