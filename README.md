# Django

Django is a python framework used for web applications .
Django software architect is MVT (Model View Template) similar to MVC(Model View Controller).But in MVT the view is the controller in mvc and template is the view in the mvc.
![alt text](https://i0.wp.com/techvidvan.com/tutorials/wp-content/uploads/sites/2/2021/06/Control-Flow-Of-MVT.jpg?ssl=1 "MVT")

# Install Django on your pc :

First you need to create a virtual enviroment (like a container) to install your dependencies

```python
python3 -m venv venv
```

on Linux to activate the virtual enviroment

```python
source venv/bin/activate
(venv) $ _
```

on Windows to activate the virtual enviroment

```python
venv\Scripts\activate
(venv) $ _
```

- now you install your dependencies

```python
pip install django
```

- check if django has been installed successfully

```python
django-admin --version
```

- create a django project

```python
django-admin startproject projectname
```

- start server

```python
python manage.py runserver
```

## Django handle the HTTP request

HTTP Requests :

- GET
- POST
- PUT
- DELETE
- HEAD
- CONNECT
- OPTION
- TRACE
- PATCH

## Django for Dynamic website

django uses Jinja for making your static html more dynamic (like blade in laravel)

some syntax you can use in your html file are:

- For Loop

```python
{% for card in cards %}
{% endfor %}
```

- Condition

```python
{% if card %}
{%else %}
{% endif %}
```

- To load from static folder and from a specific folder in static

```python
{% load static %}
{% static "img" as baseUrl %}
```

## ORM

What is ORM ?
Object–relational mapping (ORM, O/RM, and O/R mapping tool) in computer science is a programming technique for converting data between incompatible type systems using object-oriented programming languages. This creates, in effect, a "virtual object database" that can be used from within the programming language. There are both free and commercial packages available that perform object–relational mapping, although some programmers opt to construct their own ORM tools.
![alt text](https://engineertodeveloper.com/wp-content/uploads/2021/01/django_orm_diagram_1.png "ORM")
