x = 75
user_num = 0
cnt = 0

while True:
    user_num = int(input('Я загадал число от 1 до 100. Угадайте его: '))
    cnt += 1
    if user_num == x:
        print(f'Ты угадал число за {cnt} попыток')
        print('Спасибо за игру')
        break
    elif user_num > x:
        print('Загаданное число меньше')
    else:
        print('Загаданное число больше')
