

# tfg_webapp

TFG WebApp is a web application that contains the Python application developed in my [TFG repository](http://github.com/franloza/tfg). It is built with [Python][0] using the [Django Web Framework][1].

This project has the following basic apps:

* TFG WebApp: Web application that extract glucose patterns collected by FreeStyle device using decision trees. It uses
blocks defined by the meals and tries to detect risk situations in the next block.


## Installation

### Quick start

To set up a development environment quickly, first install Python 3. It
comes with virtualenv built-in. So create a virtual env by:

    1. `$ python3 -m venv tfg_webapp`
    2. `$ . tfg_webapp/bin/activate`

Install all dependencies:

    pip install -r requirements.txt

Run migrations:

    python manage.py migrate

### Detailed instructions

Take a look at the docs for more information.

[0]: https://www.python.org/
[1]: https://www.djangoproject.com/
