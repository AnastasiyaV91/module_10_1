from time import sleep
from datetime import datetime
from threading import Thread

def wite_words(word_count, file_name):                     # Функция, которая открывает файл file_name
                                                           # (или создает, если его нет) с кодировкой utf-8
    with open(file_name, 'a', encoding='utf-8') as file:
        for i in range(word_count):                        # Цикл, дописывающий в file_name каждое i word_count
            file.write(f"Какое-то слово № {i} + \n")       # количество раз
            sleep(0.1)                                     # Задержка 0.1 сек
    print(f"Завершилась запись в файл {file_name}")        # Выводим в консоль сообщение

# -------------------------- Запуск функций по заданию --------------------

time_start1 = datetime.now()    #  Текущее время - время старта функций

wite_words(10, "example1.txt")
wite_words(30, "example2.txt")
wite_words(200, "example3.txt")
wite_words(100, "example4.txt")

time_end1 = datetime.now()                  #  Текущее время - время окончания работы функции
time_res1 = time_end1 - time_start1         #  Высчитываем время работы функции
print(f"Время работы функции {time_res1}")  #  Выводим в консоль время работы функции

# -------------------------- Создание и запуск потоков --------------------

first = Thread(target=wite_words, args=(10, "example5.txt"))     # Создание первого потока
second = Thread(target=wite_words, args=(30, "example6.txt"))    # Создание второго потока
third = Thread(target=wite_words, args=(200, "example7.txt"))     # Создание третьего потока
forth = Thread(target=wite_words, args=(100, "example8.txt"))     # Создание четвертого потока

time_start2 = datetime.now()  #  Текущее время - время старта потоков

first.start()   #  Запуск первого потока
second.start()  #  Запуск второго потока
third.start()   #  Запуск третьего потока
forth.start()   #  Запуск четвертого потока

first.join()   #  Ждем завершения первого потока
second.join()  #  Ждем завершения второго потока
third.join()   #  Ждем завершения третьего потока
forth.join()   #  Ждем завершения четвертого потока
                   #  -> По завершению всех потоков программа пойдет дальше

time_end2 = datetime.now()                   #  Текущее время - время окончания работы потоков
time_res2 = time_end2 - time_start2          #  Высчитываем время работы потоков
print(f"Время работы потоков {time_res2}")   #  Выводим в консоль время работы потоков