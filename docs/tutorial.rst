========
Tutorial
========



1. Install Cookiecutter_.
2. Create project template.

.. code-block:: bash

    cookiecutter https://github.com/stefanitsky/cookiecutter-django-minimal.git
    project_name [My Project]: My Personal Blog
    project_slug [my_personal_blog]: blog
    author [Alexandr Stefanitsky-Mozdor]:
    email [stefanitsky.mozdor@gmail.com]:
    version [0.1.0]:
    timezone [UTC]: Europe/Moscow

3. Open created folder.

.. code-block:: bash

    cd blog

4. Run project via ready-to-use docker_ and make_.

.. code-block:: bash

    make development-up

5. Open http://0.0.0.0:8000/.


.. _Cookiecutter: https://cookiecutter.readthedocs.io/en/latest/installation.html
.. _docker: https://www.docker.com/
.. _make: https://www.gnu.org/software/make/