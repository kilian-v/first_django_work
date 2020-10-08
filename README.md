# Django Training

This is a very simple website built with Django.

---

## Running the project

To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with

```
pip install virtualenv
```

Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project

```
virtualenv env
```

That will create a new folder `env` in your project directory. Next activate it with this command on mac/linux:

```
source env/bin/active
```

Then install the project dependencies with

```
pip install -r requirements.txt
```

Now you can run the project with this command

```
python manage.py runserver
```

Used links

```
https://www.digitalocean.com/community/tutorials/django-authentication-with-facebook-instagram-and-linkedin#step-2-—-facebook-authentication

https://www.youtube.com/watch?v=YZvRrldjf1Y&t=937s
```