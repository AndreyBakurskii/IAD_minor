from random import randint

N = int(input("Введите максимальное число, которое я могу загадать? "))

mystery_number = randint(1, N)


user_answer = 0
counter = 0

print("!!! Игра началась !!!")

while user_answer != mystery_number:

    counter += 1

    user_answer = int(input("Введите ваше число: "))

    if user_answer > mystery_number:
        print("Ваше число больше загаданного")

    elif user_answer < mystery_number:
        print("Ваше число меньше загаданного")

    else:
        print(f"Вы выиграли!! Загаданное число: {mystery_number}\nКоличество попыток: {counter}")
        break

