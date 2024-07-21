def array_diff(a, b):
    # Создаем новый список, содержащий только элементы из списка a, которые не встречаются в списке b
    result = [x for x in a if x not in b]
    
    return result
