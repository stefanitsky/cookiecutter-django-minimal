===========================
cookiecutter-django-minimal
===========================

.. image:: https://readthedocs.org/projects/cookiecutter-django-minimal/badge/?version=latest
    :target: https://cookiecutter-django-minimal.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status


A cookiecutter template for creating minimal Django apps, with configured settings for multiple environments.

* Documentation: https://cookiecutter-django-minimal.readthedocs.io/en/latest/


Highlights
----------
* Minimal setup: Django 3 with ASGI_ & PostgreSQL 11.6.
* Preconfigured settings & compose files for multiple environments.
* Configuration as in the RoR application for main app folder.


========
Features
========

Project structure
-----------------
The project structure is similar to RoR_ project structure, where application is in one folder.
Templates, static files, fixtures, media - everything is configured to be stored in the folder with the main application.

Bump versions
-------------
The project has a configured version controller - bump2version_

Usage_:

.. code-block:: bash

    bump2version [options] part [file]


It changes the version for the project, including sentry_.


Makefile
--------
Makefile contains many convenient and useful commands. You can get a complete list of commands by typing ``make help``.


.. _bump2version: https://github.com/c4urself/bump2version
.. _Usage: https://github.com/c4urself/bump2version#usage
.. _sentry: https://docs.sentry.io/
.. _RoR: https://rubyonrails.org/
.. _ASGI: https://docs.djangoproject.com/en/3.0/topics/async/