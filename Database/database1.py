import sqlite3

base = sqlite3.connect('inno.db')
cur = base.cursor()

base.execute(
    'CREATE TABLE IF NOT EXISTS {}(id INTEGER PRIMARY KEY, name TEXT, author TEXT, genre TEXT,'
    '"the year of publishing" INTEGER)'.format('books')
)
base.commit()

base.execute(
    'CREATE TABLE IF NOT EXISTS {}(id INTEGER PRIMARY KEY, Название TEXT, Описание TEXT,'
    '"Дата начала" DATE, "Дата окончания" DATE, Статус TEXT)'.format('tasks')
)
base.commit()

base.execute(
    'CREATE TABLE IF NOT EXISTS {}(id INTEGER PRIMARY KEY, название TEXT, режиссер TEXT, "год выпуска" INTEGER,'
    'рейтинг DECIMAL, длительность INTEGER)'.format('Фильмы')
)
base.commit()