# Ввод количества сотрудников
while True:
    try:
        n = int(input('Введите количество сотрудников: '))
    except ValueError:
        print('! Ошибка ! Введите целое число')
    else:
        break

# Ввод расстояний
distances = [0] * n
for i in range(n):
    worker_number = i + 1
    while True:
        try:
            distances[i] = int(input(f'Введите расстояние (км) до дома для сотрудника № {worker_number}: '))
        except ValueError:
            print('! Ошибка ! Введите целое число')
        else:
            break

# Ввод тарифов
rates = [0] * n
for j in range(n):
    taxi_number = j + 1
    while True:
        try:
            rates[j] = int(input(f'Введите cтоимость (руб) за проезд одного километра для такси № {taxi_number}: '))
        except ValueError:
            print('! Ошибка ! Введите целое число')
        else:
            break

# Расчет минимальных затрат
distances_s = list(distances)
rates_s =  list(rates)
distances.sort()
rates.sort(reverse=True)
total_sum = 0
data = [0] * n
for a in range(n):
    cost = distances[a] * rates[a]
    total_sum = total_sum + cost
    data[distances_s.index(distances[a])] = rates_s.index(rates[a]) + 1
    distances_s[distances_s.index(distances[a])] = 0
    rates_s[rates_s.index(rates[a])] = 0

#Функции для перевода стоимости в слова
def get_number_word(number):
    units = ['', 'один', 'два', 'три', 'четыре', 'пять',
             'шесть', 'семь', 'восемь', 'девять', 'десять',
             'одиннадцать', 'двенадцать', 'тринадцать',
             'четырнадцать', 'пятнадцать', 'шестнадцать',
             'семнадцать', 'восемнадцать', 'девятнадцать']
    tens = ['', 'десять', 'двадцать', 'тридцать', 'сорок',
            'пятьдесят', 'шестьдесят', 'семьдесят',
            'восемьдесят', 'девяносто']
    hundreds = ['', 'сто', 'двести', 'триста', 'четыреста',
                'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']

    if number == 0:
        return 'ноль'

    if number < 20:
        return units[number]

    if number < 100:
        return tens[number // 10] + ' ' + units[number % 10]

    if number < 1000:
        if number % 100 == 0:
            return hundreds[number // 100]
        else:
            return hundreds[number // 100] + ' ' + get_number_word(number % 100)
    
    if number < 100000:
        if number < 10000:
            if (number // 1000) == 1:
                hundreds_word = 'одна тысяча '
            elif (number // 1000) == 2:
                hundreds_word = 'две тысячи '
            elif (number // 1000) == 3:
                hundreds_word = 'три тысячи '
            elif (number // 1000) == 4:
                hundreds_word = 'четыре тысячи '
            else:
                hundreds_word = units[(number // 1000) % 10] + ' тысяч '

            if number % 1000 == 0:
                return hundreds_word
            else:
                return hundreds_word + get_number_word(number % 1000)
        else:
            if (number // 1000) % 10 == 1:
                hundreds_word = 'одна тысяча '
            elif (number // 1000) % 10 == 2:
                hundreds_word = 'две тысячи '
            elif (number // 1000) % 10 == 3:
                hundreds_word = 'три тысячи '
            elif (number // 1000) % 10 == 4:
                hundreds_word = 'четыре тысячи '
            else:
                hundreds_word = units[(number // 1000) % 10] + ' тысяч '

            if number % 10000 == 0:
                return tens[number // 10000] + ' тысяч '
            else:
                return get_number_word(int(str(number // 1000)[0] + '0')) + hundreds_word + get_number_word(number % 1000)

    if number == 100000:
        return 'сто тысяч'
        

def get_currency_word(number):
    if 10 < number % 100 < 20:
        return 'рублей'

    if number % 10 == 1:
        return 'рубль'

    if 1 < number % 10 < 5:
        return 'рубля'

    return 'рублей'

# Преобразуем число в слова
number_word = get_number_word(total_sum)

# Определяем правильное окончание для валюты
currency_word = get_currency_word(total_sum)

# Вывод результатов
for x in data:
    print(x)
print(total_sum)
print(number_word, currency_word)