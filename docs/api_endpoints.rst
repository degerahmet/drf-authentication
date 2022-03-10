.. _api_endpoints:

API endpoints
=============

Basic
--------



* /auth/login/ (POST)

    * email
    * password

    Returns Token key

* /auth/token/refresh/ (POST)
    * refresh_token

* /auth/logout/ (POST)

* /auth/logoutall/ (POST)

* /auth/user/ (POST)

    * email

* /auth/request-password-reset-email/ (POST)

    * email

* /auth/check-password-reset/<uidb64>/<token>/ (GET)

* /auth/complete-password-reset/ (POST)

    * uid64
    * token
    * password

    .. note:: uid64 and token are sent in email after calling /auth/request-password-reset-email/

* /auth/change_password/ (POST)

    * new_password1
    * new_password2
    * old_password


* /auth/user/ (GET)

    * username
    * first_name
    * last_name

    Returns pk, username, email, first_name, last_name


* /auth/user/ (GET, PATCH)

    * first_name
    * last_name

    Returns pk, username, email, first_name, last_name


Registration
-------------

* /auth/registration/ (POST)

    * username
    * password1
    * password2
    * email

