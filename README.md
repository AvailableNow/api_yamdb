### ЯП - Спринт 10 - Проект YaMDb (групповой проект).
### Описание
Проект YaMDb собирает отзывы (Review) пользователей на произведения (Title).
Произведения делятся на категории: «Книги», «Фильмы», «Музыка».
Список категорий (Category) может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).

Команда разработки:
- :white_check_mark: Auth/Users: [Илья Шунин](https://github.com/AvailableNow)
- :white_check_mark: Titles/Category/Genre: [Евгений Иванов](https://github.com/Iv-EN)
- :white_check_mark: Reviews/Comments: [Кристина Скоринова](https://github.com/Kristina-kul)

Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

В каждой категории есть произведения: книги, фильмы или музыка. Например, в категории «Книги» могут быть произведения «Винни Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Насекомые» и вторая сюита Баха. Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). Новые жанры может создавать только администратор.

Благодарные или возмущённые читатели оставляют к произведениям текстовые отзывы (Review) и выставляют произведению рейтинг (оценку в диапазоне от одного до десяти). Из множества оценок автоматически высчитывается средняя оценка произведения.

Полная документация к API находится по эндпоинту /redoc

### Стек технологий использованный в проекте:
- Python 3.7
- Django 2.2.28
- DRF
- JWT

# api_yamdb
api_yamdb
# Описание и установка проекта API_YAMDB
Это командный проект, в котором описаны конечные точки API для сайта с отзывами на кино, музыку и книги.
С помощью этих конечных точек можно полностью интегрировать функционал сайта в свое приложение.

Я занимался разработкой кастомной модели пользователя, регистрации и подтверждения через E-mail, реализовал работу с токеном и права доступа. 

## Установка и запуск проекта
1. Установите python
[вот ссылка](https://www.python.org/downloads/).

2. В комнадной строке клонируйте этот репозиторий на компьютер:
```
$ git clone git@github.com:AvailableNow/api_yamdb.git
```

3. Перейдите в папку api_yamdb
```
$ cd api_yamdb
```

4. Создайте и активируйте виртуальное окружение:
```
$ python -m venv venv (windows)
$ python3 -m venv venv (mac)

$ source venv/Scripts/activate (windows)
$ source venv/bin/activate (mac)
```

5. Установите зависимости проекта:
```
$ python -m pip install --upgrade pip

$ pip install -r requirements.txt
```

6. Выполните миграции:
```
$ python manage.py migrate
```

7. Запустите проект:
```
$ python manage.py runserver
```

#### Сейчас проект должен быть доступен по адресу: http://127.0.0.1:8000/api/v1/
#### Документация API проекта: http://127.0.0.1:8000/redoc/

### Импорт данных из csv для наполнения базы:

Запустите команду импорта:

```
python manage.py load_csv_data
```

В терминале отобразится результат импорта.<br>
Если какой-либо из файлов отсутствует, то он не будет импортирован.

Примеры файлов csv для наполнения базы находятся в папке /api_yamdb/static/data/*.csv:
- users.csv - файл для заполнения таблицы пользователей
- titles.csv - файл для заполнения таблицы произведений.
- category.csv - файл для заполнения таблицы категорий произведений.
- genre.csv - файл для заполнения таблицы жанров произведений.
- genre_title.csv - файл для заполнения таблицы Many-to-Many: одно произведение может иметь несколько жанров.
- review.csv - файл для заполнения таблицы отзывов к произведениям.
- comments.csv - файл для заполнения таблицы комментариев к отзывам.
<br>
