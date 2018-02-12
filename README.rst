passage
=======

A Django project for exploring ways to display digital text with the purpose of creating a gospel study app.

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django


:License: BSD

Why
---

This project is inspired by instruction found in a [CES devotional given by Elder David A. Bednar on February 4, 2007 entitled `*A Reservoir of Living Water* <http://media.ldscdn.org/pdf/ces-firesides/2007-ces-firesides-for-young-adults/2007-02-0010-a-reservoir-of-living-water-eng.pdf>`_.

Elder Bednar (2007) identifies three ways to obtain living water from the scriptures. They include:

1. "*[R]eading* the scriptures from beginning to end"
2. "*[S]tudying* the scriptures by topic"
3. "*[S]earching* the scriptures for connections, patterns, and themes"

This project is structured to follow these three methods for obtaining living water:

1. Digital text display
2. Gospel study topics
3. Identifying connections, patterns, and themes

References
^^^^^^^^^^

Bednar, D. A. (2007). A reservoir of living water. *CES Fireside for Young Adults*, February 4, 2007. Retrieved from `<https://www.lds.org/broadcasts/archive/ces-devotionals/2007/01>`_

Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run manage.py test
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ py.test

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html





Deployment
----------

The following details how to deploy this application.




