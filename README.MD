# Batch Loading One-to-Many Data Model


Navigate into the `batch` folder

    cd batch

Install django extenstions

    pip install django_extensions

Check if there are no errors

    python manage.py check

Makemigration - create the migration python files based on the model.py file structure

    python manage.py makemigrations

Migrate - create/update the database structure/scheme based on the migration python files

    python manage.py migrate

Run the script

    python3 manage.py runscript many_load


## Check the data in the admin interface

    python manage.py createsuperuser


And enter the username and password

Then go to localhost: 127.0.0.1/admin

## Check the data in the DB Browser SQLite

Download and install the software from [https://sqlitebrowser.org/](https://sqlitebrowser.org/)