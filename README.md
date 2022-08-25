# Project
Environment Setup 🚀

$ git clone https://github.com/Rajat1811/Project.git

$ cd Assignment/

If virtualenv is not installed (What is virtualenv?):

$ pip install virtualenv

Create a virtual environment

$ virtualenv env

Activate the environment everytime you open the project

$ source env/Scripts/activate

Install requirements 🛠

$ pip install -r requirements.txt

Run migrations for Database

$ python manage.py makemigrations

$ python manage.py migrate

Create superuser for Admin Login 🔐

$ python manage.py createsuperuser

Enter your desired username, email and password. Make sure you remember them as you'll need them in future.

eg.

Username: admin

Email: admin@admin.com

Password: HighlyConfidentialPassword
All Set! 🤩

Now you can run the server to see your application up & running 🚀

$ python manage.py runserver