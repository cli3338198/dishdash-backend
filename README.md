# DishDash Backend

- A demo app for practicing Django and deploying to Amazon EC2.
- An API that returns a recipe and information on the ingredients.

## Django/Python Notes & Commands

- Create a virtual environment

```
python -m venv venv
```

- Activate

```
.\venv\Scripts\Activate.ps1
```

- Deactivate

```
.\venv\Scripts\deactivate.ps1
```

- Freeze requirements

```
pip freeze > requirements.txt
```

- Install requirements

```
pip install -r requirements.txt
```

- Access django commands

```
django-admin
```

- Start project

```
django-admin startproject <PROJECT NAME> <PORT NUMBER>
```

- Start server

```
python .\manage.py runserver <PORT NUMBER>
```

- Create API app in django

```
python manage.py startapp api
```

- Register 'api' to installed apps in settings.py

```py
INSTALLED_APPS = [
    ...
    'api'
]
```

- Run server

```
python .\manage.py runserver 9000
```

## Endpoints

```
http://localhost:<PORT NUMBER>/api/hello

```

```

http://localhost:<PORT NUMBER>/api/recipes/?q=chicken

```

```

http://localhost:<PORT NUMBER>/api/ingredient/?ingredient=lettuce

```
