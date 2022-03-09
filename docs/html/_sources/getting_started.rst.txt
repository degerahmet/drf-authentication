.. _getting_started:

Getting started
===============

Requirements
------------

* Python (3.7, 3.8, 3.9, 3.10)
* Django (2.2, 3.1, 3.2)
* Django REST Framework (3.10, 3.11, 3.12)

These are the officially supported python and package versions.  Other versions
will probably work.  You're free to modify the tox config and see what is
possible.

Installation
------------

Django Rest Framework Authentication can be installed with pip::
  pip install drf-auth-simple

This package provides 4 different module.
 * Authentication with JWT (drf_auth_jwt)
 * Authentication with Knox (drf_auth_knox)
 * Authentication with JWT & Custom User Model (drf_auth_jwt_cu)
 * Authentication with Knox & Custome User Model (drf_auth_knox_cu)


If you use Authentication with Custom User Model(JWT or Knox)
Then, your django project must be configured to use the library.  In ``settings.py``, add
``AUTH_USER_MODEL``.


For JWT 

.. code-block:: python

  AUTH_USER_MODEL = 'drf_auth_jwt_cu.User'

For Knox 

.. code-block:: python
  AUTH_USER_MODEL = 'drf_auth_knox_cu.User'


Custom User Model: 
.. code-block:: python


class User(AbstractBaseUser):
    username    = None

    first_name = models.CharField(max_length=255,null=True,blank=True)
    last_name = models.CharField(max_length=255,null=True,blank=True)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email   

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return True
    
    def __str__(self):
        return self.email


    def get_full_name(self):
        return str(self.first_name + self.last_name)

    def get_short_name(self):
        return self.first_name
