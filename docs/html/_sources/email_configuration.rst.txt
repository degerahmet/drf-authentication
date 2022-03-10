.. _email_configuration:


EMAIL CONFIGURATION
====================

Your django project must be configured to use the library.  In ``settings.py``, add
``EMAIL_BACKEND``.


For JWT 

.. code-block:: python

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    