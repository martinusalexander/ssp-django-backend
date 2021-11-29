# SSP Django Backend

# Requirements
- Python 3.8
- Anaconda
- MySQL 5.7

# Installation

## Install the Python project
Clone the project
```
cd <your source code folder>
git clone git@github.com:martinusalexander/ssp-django-backend.git
cd ssp-django-backend
git checkout init_dev
```

Activate the Conda environment (or optionally create a new one)
```
conda create --name my-backend-env python=3.8
conda activate my-backend-env
```

Install the Python requirements using `pip`
```
pip install -r requirements.txt
```

## Setup the MySQL database
Setup a new MySQL database (run it from your favorite MySQL GUI tools)
```
CREATE DATABASE `solusisparepart`
```
Change the database credentials in `solusisparepart/settings.py`
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'solusisparepart',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

## Run the database migrations
```
python manage.py migrate
```

## Start the Python server
```
python manage.py runserver
```

# Test the Django REST framework
Create a superuser
```
python manage.py createsuperuser
# Then please fill in the prompt
```

Query the created user (one option can be `curl`)
```
curl -H 'Accept: application/json; indent=4' -u myemail:mypassword http://127.0.0.1:8000/users/
```
Alternatively, you can use other tools like [Postman](https://www.postman.com/)

You should see the API response in the following format
```
[
    {
        "full_name": "Myname",
        "email": "myname@example.com"
    }
]
```
