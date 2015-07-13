.. contents::

============================
Django Spam Referral Blocker
============================

Information
===========

.. image:: https://travis-ci.org/avara1986/django-blockreferralspam.svg
    :target: https://travis-ci.org/avara1986/django-blockreferralspam


.. image:: https://coveralls.io/repos/avara1986/django-blockreferralspam/badge.svg?branch=master&service=github 
    :target: https://coveralls.io/github/avara1986/django-blockreferralspam?branch=master



Django Spam Referral Blocker removes all Spam in your Google Analytics statics. You could find many tutorials to remove referral SPAM with .htaccess, apache, nginx.

.. image:: https://cdn.checkfront.com/wp-content/uploads/2015/03/google-analytics-icon.png

If you deploy your website in Google App Engine, this App could help you.

.. image:: http://www.appscale.com/wp-content/uploads/2013/10/google-app-engine-logo.png


**Django Spam Referral Blocker** use `This blacklist <https://github.com/piwik/referrer-spam-blacklist>`_

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