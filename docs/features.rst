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
