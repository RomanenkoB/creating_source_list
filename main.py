from helpers import get_book_source

"""Вызовите функцию get_book_source, которая принимает возможное название книги и количество источников"""

# get_book_source("Python", 3)

book = str(input("Введи книгу: "))
count = int(input("Введи количество источников: "))
print(" ")

try:
    get_book_source(book, count)
except:
    print("Извинись!")

print(" ")
input("Введи любой символ для выхода: ")