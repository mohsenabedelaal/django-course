![alt text](https://res.cloudinary.com/practicaldev/image/fetch/s--jbr__sKh--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/d0hst9r97gq50860kpq0.png "Django")

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
