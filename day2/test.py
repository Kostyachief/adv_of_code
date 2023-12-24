import re

# Исходный список строк
list_of_values = ["день 13", "день 12", "час 2", "день 4"]

# Функция для извлечения цифр из строки
def extract_digits(s):
    return ''.join(re.findall(r'\d+', s))

# Применение функции к каждой строке в списке
digits_only = [extract_digits(value) for value in list_of_values]

# Вывод результатов
print(digits_only)
