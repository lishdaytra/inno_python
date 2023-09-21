from django.db import models


# Просто пример для создания
'''class Position(models.Model):

    def __repr__(self):
        return print(''''''
        Имя класса = Имя таблицы (main_position) Имя приложения + Название класса
        название переменной = название столбца в таблице БД
        python manage.py makemigrations -создает файл в которой описывается, что будет добавлено
            после миграции
        Если такой таблице в БД нет, то Django её создаст сама
        '''''')

    title = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField()
    quantity = models.IntegerField()
    chef = models.ForeignKey('Chef', on_delete=models.CASCADE, null=True, default=None)
class Chef(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()

class RandomTable(models.Model):
    title = models.CharField(max_length=255)'''

class Author(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    born = models.DateField(default='2000-01-01',auto_now=False, auto_now_add=False)

class Books(models.Model):

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date_of_publication = models.DateField(default='2000-01-01', auto_now=False, auto_now_add=False)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)