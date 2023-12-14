from word2number import w2n

with open('cal_doc.txt', 'r') as file:
    # обьявляем список для результирующей суммы
    DigitsSum = 0
    # пробегаем построчно по файлу
    for line in file:
        #number = w2n.word_to_num(line)
        #print(line)
        # список с цифрами 
        digits = [char for char in line if char.isdigit()]
        # добавляем в общую сумму значение
        DigitsSum = DigitsSum + int(digits[0]+digits[-1])
print(DigitsSum)