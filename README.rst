.. contents::

============================
Django Spam Referral Blocker
============================

Information
===========

.. image:: https://travis-ci.org/avara1986/django-blockreferralspam.svg
    :target: https://travis-ci.org/avara1986/django-blockreferralspam


.. image:: https://coveralls.io/repos/avara1986/django-blockreferralspam/badge.png
  :target: https://coveralls.io/r/avara1986/django-blockreferralspam


.. image:: https://badge.fury.io/py/django-blockreferralspam.png
    :target: https://badge.fury.io/py/django-blockreferralspam

.. image:: https://pypip.in/d/django-blockreferralspam/badge.png
    :target: https://pypi.python.org/django-blockreferralspam/pitble


Django Spam Referral Blocker remove all Spam in your Google Analytics statics. You could find many tutorials to remove referral SPAM with .htaccess, apache, nginx.

If you deploy your website in Google App Engine, this App could help you

.. image:: http://www.appscale.com/wp-content/uploads/2013/10/google-app-engine-logo.png

It use `This blacklist <https://github.com/piwik/referrer-spam-blacklist>`_

Installation
============

* In your settings:

::

    INSTALLED_APPS = (
        ...
        'blockreferralspam',
    )

    MIDDLEWARE_CLASSES = (
        ...
        'blockreferralspam.middleware.KillSpam',
    )
