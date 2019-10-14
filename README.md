

# tfg_webapp

TFG WebApp is a web application that contains the Python application developed in my [TFG repository](http://github.com/franloza/tfg). It is built with [Python][0] using the [Django Web Framework][1].

This project has the following basic apps:

* TFG WebApp: Web application that extract glucose patterns collected by FreeStyle device using decision trees. It uses
blocks defined by the meals and tries to detect risk situations in the next block.


## Quickstart 

```
git clone https://github.com/franloza/tfg_webapp.git --recursive
cd tfg_webapp
docker-compose up
```

Webpage will be available at `localhost:8000`

### Development

To set up a development environment quickly, first install Python 3.6. Later,
install the dependencies using:

`pipenv install --dev`

You can use a Docker image of PostgreSQL to run the database or SQLlite (See config/local.example.dev). Once you have chosen the database, run migrations:

    python manage.py migrate

### Detailed instructions

Take a look at the docs for more information.

[0]: https://www.python.org/
[1]: https://www.djangoproject.com/
