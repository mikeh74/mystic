# Example Django site

This is a simple Django site to show the basic aspects of Django.

## Getting started

Once you have cloned the repo locally then run the following in the terminal:

```bash

# switch working directory the folder containing this file
cd ~/path/to/mysite

# create a virtual environment
python -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install the dependencies
pip install -r requirements.txt

# create a superuser account
python manage.py createsuperuser

# Run migrations
python manage.py migrate

# Run the development server:
python manage.py runserver

```

Once you have run these commands you can open this web page:

<http://localhost:8000>

And go here to login to the admin panel:

<http://localhost:8000/admin>


## Tasks to complete

Update the template mysite/templates/base.html to include the header and footer
sections, references to bootstrap and other requirements.

Update the template news/templates/news/news_list.html to show a list of cards
as per the designs you have been working on.

Update the news/views.py news_detail function so that it returns the correct
news article for the template.

Update the news/templates/news/news_detail.html template so that it reflects
the designs you have been working on.
