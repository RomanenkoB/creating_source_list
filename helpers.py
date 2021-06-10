from env import url, url_book
import requests
from bs4 import BeautifulSoup
import random

book = {
    "name_book": "",
    "author": "",
    "publisher": "",
    "year": "",
    "pages": "",
    "isbn": ""
}

list_city = ["Москва", "Санкт-Петербург", "Самара", "Ростов-на-Дону", "Самара", "Казань", "Новосибирск", "Екатеринбург", "Воронеж"]


def get_book_source(book_name, count):
    """ Данные берутся из сайта Лабиринт, если возникает эксепшен то увы извиняйте """

    r = requests.get(url=url.format(book_name))
    soup = BeautifulSoup(r.text, 'lxml')
    for i in range(count):
        firs_cart = soup.find_all('div', class_="card-column")[i]
        cart_book = firs_cart.find('div', class_="product")
        name_book = cart_book.attrs["data-name"]
        id_book = cart_book.attrs["data-product-id"]
        author, publisher, year, pages, isbn = get_description(id_book)
        book["name_book"] = name_book
        book["author"] = author
        book["publisher"] = publisher
        book["year"] = year
        book["pages"] = pages
        book["isbn"] = isbn
        # print(book)
        if (len(author.split(" ")) > 2):
            result = book["author"] + book["name_book"] + ". / " + book["author"].split(" ")[1] + " " + book["author"].split(" ")[2] +\
                     " " + book["author"].split(" ")[0] + " - " + random.choice(list_city) + ": " + book["publisher"] + " " + book["year"] + ". - C. " \
                     + book["pages"] + ". - " + book["isbn"]
        else:
            result = book["author"] + book["name_book"] + ". / " + book["author"].split(" ")[1] + " " + \
                     book["author"].split(" ")[0] + " - " + random.choice("list_city") + ": " + book[
                         "publisher"] + " " + book["year"] + ". - C. " \
                     + book["pages"] + ". - " + book["isbn"]
        print(result)


def get_description(id):
    r = requests.get(url=url_book.format(id))
    soup = BeautifulSoup(r.text, 'lxml')
    description = soup.find('div', class_="product-description")
    author_mass = description.find('div', class_="authors").find("a", class_="analytics-click-js").attrs["data-event-content"].split(" ")
    author = author_mass[0] + " "
    for i in range(1, len(author_mass)):
        author += author_mass[i][:1] + ". "
    publisher = description.find('div', class_="publisher").find("a", class_="analytics-click-js").attrs["data-event-content"]
    year = description.find('div', class_="publisher").text.split(", ")[-1][:-1]
    pages = description.find('div', class_="pages2").text.split(": ")[1].split(" ")[0]
    isbn = description.find('div', class_="isbn").text
    return author, publisher, year, pages, isbn

