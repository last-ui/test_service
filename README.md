
<h1 align="center"> Testing Task </h1>

___
### Используемый стек<a name="stack"></a>

[![Python][Python-badge]][Python-url]
[![Django][Django-badge]][Django-url]
[![DRF][DRF-badge]][DRF-url]
[![Vue.js][Vue-badge]][Vue-url]

### Системные требования
- Python 3.11+;
- Node.js (v20.9.0+);
- [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer).

### Архитектура проекта<a name="architecture"></a>

| Директория     | Описание              |
|----------------|-----------------------|
| `frontend`     | Фронтенд Vue.js       |
| `backend`      | Код Django приложения |
| `backend/test` | Код класса Test       |

<h2>Подготовка проекта к запуску</h2>

1. Заполнить .env-файл, вариант заполнения указан example.env.

2. Создать виртуальное окружение проекта с помощью команды:
```SHELL
poetry install
```
- либо установить зависимости из файла requirements.txt:

```SHELL
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```
3. Применить миграции:
```SHELL
python backend/manage.py migrate
```
4. Установить зависимости frontend-а:

```SHELL
cd frontend
npm install
```

<h2>Запуск проекта</h2>

1. Из корневой папки запустить командой:

```shell
npm run --prefix frontend dev & python backend/manage.py runserver
```
2. Проект будет доступен по адресу http://localhost:5173/

4. Тестовый класс Test /backend/test/test.py:
```SHELL
# Создание объекта
test_object = Test(question_count=<int>, result_count=<int>)

# Метод получения вопросов с внешнего API и сохранения в БД
test_object.create_new_questions()

#Метод получения записей в категории
test.get_category_question_count(category=<str>)

#Метод получения вопросов из БД и сохранения в json файл.
test.get_db_questions()
```


<!-- MARKDOWN LINKS & BADGES -->

[Python-url]: https://www.python.org/

[Python-badge]: https://img.shields.io/badge/Python-376f9f?style=for-the-badge&logo=python&logoColor=white

[Django-url]: https://github.com/django/django

[Django-badge]: https://img.shields.io/badge/Django-0c4b33?style=for-the-badge&logo=django&logoColor=white

[DRF-url]: https://github.com/encode/django-rest-framework

[DRF-badge]: https://img.shields.io/badge/DRF-a30000?style=for-the-badge

[Vue-url]: https://vuejs.org/index.html

[Vue-badge]: https://img.shields.io/badge/Vue.js-4FC08D?style=for-the-badge&logo=vue.js&logoColor=white
