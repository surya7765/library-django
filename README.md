# Library Managment using Django

Create a project using django-admin and then set configuration. Add `.env` file inside folder where you can see `settings.py`. Genereate a random secret key using secret package from python and paste `SECRET_KEY` = "<<value>>" here.

Now run `py manage.py runserver` command inside folder. I believe now you can see the page in your default browsers. 

To get access of the admin panel run `py manage.py createsuperuser` command and now give enter a username as well as email*(required).

