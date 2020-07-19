# -*- coding: utf-8 -*-

import json
from csv import DictReader


USERS_PATH = 'data/users.json'
BOOKS_PATH = 'data/books.csv'
EXAMPLE_PATH = 'data/example.json'
OUTPUT_JSON_FILE = 'data/users_with_books.json'


def create_users_with_books_empty_dict(path):
    with open(path, 'r') as f:
        keys = json.load(f).keys()

    users_with_books_empty_dict = dict.fromkeys(keys)
    return users_with_books_empty_dict


def create_books_list(path):
    books_list = []
    with open(path, newline='') as f:
        reader = DictReader(f)

        for row in reader:
            book_dict = dict()
            book_dict["title"] = row["Title"]
            book_dict["author"] = row["Author"]
            book_dict["height"] = row["Height"]

            books_list.append(book_dict)

    return books_list


def write_users_with_books_json(path, data):
    with open(path, "w") as f:
        s = json.dumps(data, indent=4)
        f.write(s)


if __name__ == '__main__':
    
    # создаем пустой словарь по образцу из example.json
    users_with_books_empty_dict = create_users_with_books_empty_dict(EXAMPLE_PATH)

    # преобразуем пользователей из users.json в список словарей
    users_with_books_list = []

    with open(USERS_PATH, 'r') as f:
        users = json.load(f)

        for user in users:
            users_with_books_dict = users_with_books_empty_dict.copy()
            users_with_books_dict["name"] = user["name"]
            users_with_books_dict["gender"] = user["gender"]
            users_with_books_dict["address"] = user["address"]
            users_with_books_dict["books"] = []

            users_with_books_list.append(users_with_books_dict)

    # получаем список словарей книг только с нужными ключами
    books_list = create_books_list(BOOKS_PATH)

    # добавляем книги пользователям
    for user in users_with_books_list:
        if len(books_list) > 0:
            book = books_list.pop()
            user_books = user["books"]
            user_books.append(book)
        else:
            break

    # запишем выходной файл
    write_users_with_books_json(OUTPUT_JSON_FILE, users_with_books_list)
