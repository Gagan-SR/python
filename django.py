# Install Django if needed
pip install django

# Create project and app
django-admin startproject mysite
cd mysite
python manage.py startapp hello

# Add 'hello' to INSTALLED_APPS in mysite/settings.py
# Then create migrations: python manage.py migrate
# Run dev server: python manage.py runserver
