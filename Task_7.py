 # Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.
 # Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
 # Используйте написанную ранее функцию int_func().

def int_func (n):
    sep_words = n.split(' ')
    total = []
    for i in sep_words:
        str_element = str(i)
        first_letter = str_element[:1].upper()
        word = first_letter + str_element[1:]
        total.append(word)
    return total
print(int_func("привет андрей"))