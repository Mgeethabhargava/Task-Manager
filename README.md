# Task-Manager
Task Management Application using Django

#To Setup this Project
Open cmd in project path
First Install Requirements.txt file using pip
# Run following commands to setup Database related things through migrations
python manage.py makemigrations
python manage.py makemigrations tasks
python manage.py migrate
# To Create Super User / Admin
python manage.py createsuperuser
# For Testing
python manage.py runserver

# Check this urls in Browser
http://127.0.0.1:8000 -------> for login page
http://127.0.0.1:8000/admin -----------> for admin panel [if super user is created]

