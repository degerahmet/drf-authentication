.. _knox_settings:

Knox Settings
===============

 `knox.settings`

Settings in Knox are handled in a similar way to the rest framework settings.
All settings are namespaced in the ``REST_KNOX`` setting.

Example ``settings.py``


.. code-block:: python

    # These are the default values if none are set
    
    from datetime import timedelta
    from rest_framework.settings import api_settings
    
    REST_KNOX = {
        'SECURE_HASH_ALGORITHM': 'cryptography.hazmat.primitives.hashes.SHA512',
        'AUTH_TOKEN_CHARACTER_LENGTH': 64,
        'TOKEN_TTL': timedelta(hours=10),
        'USER_SERIALIZER': 'knox.serializers.UserSerializer',
        'TOKEN_LIMIT_PER_USER': None,
        'AUTO_REFRESH': False,
        'EXPIRY_DATETIME_FORMAT': api_settings.DATETIME_FORMAT,
    }


For full documentation, visit `Django-Rest-Knox <https://james1345.github.io/django-rest-knox/settings/>`_.
