def special_number(number):
    # Преобразуем число в строку для удобства обращения к каждой цифре
    number_str = str(number)
    
    # Считаем сумму цифр, возведенных в степень, равную позиции цифры
    total = sum(int(digit) ** (i+1) for i, digit in enumerate(number_str))
    
    # Проверяем, является ли число особенным
    if total == number:
        return True
    else:
        return False
