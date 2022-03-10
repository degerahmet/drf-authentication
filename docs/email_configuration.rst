.. _email_configuration:


Email Configuration
====================

Your django project must be configured to use the library.  In ``settings.py``, add
``EMAIL_BACKEND``.


.. code-block:: python

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

For full `Sending Email Django Documentation <https://docs.djangoproject.com/en/4.0/topics/email/>`_.