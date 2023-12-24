file = 'G:/python/adv_of_code/day1/cal_doc.txt'
# словарь с сокращениями
replacement_dict = {
    1: 'on',
    2: 'tw',
    3: 'thr',
    4: 'fou',
    5: 'fi',
    6: 'six',
    7: 'sev',
    8: 'eig',
    9: 'nin',
    10: 'ten'
                    }
with open(file, 'r') as file:
    # обьявляем список для результирующей суммы
    DigitsSum = 0
    # пробегаем построчно по файлу
    for line in file:
        for key, value in replacement_dict.items():
            # замена текста на циферку
            line = line.replace(value, str(key))
            #print(line)
        # список с цифрами
        digits = [char for char in line if char.isdigit()]
        # добавляем в общую сумму значение
        DigitsSum = DigitsSum + int(digits[0]+digits[-1])
print(DigitsSum)