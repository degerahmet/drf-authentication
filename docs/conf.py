
from pkg_resources import get_distribution

# -- General configuration ------------------------------------------------


def django_configure():
    from django.conf import settings

    settings.configure(
        SECRET_KEY="a random key to use",
        INSTALLED_APPS=(
            "django.contrib.admin",
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
            "django.contrib.sites",
            "django.contrib.staticfiles",
            "rest_framework",
            "rest_framework_simplejwt",
            "rest_framework_simplejwt.token_blacklist",
        ),
    )

    try:
        import django

        django.setup()
    except AttributeError:
        pass


django_configure()

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
]

templates_path = ["_templates"]

source_suffix = ".md"

master_doc = "index"

project = "Django Rest Framework Authentication"
copyright = "2022, Ahmet Deger"

release = get_distribution("drf-authenticaton").version

# The short X.Y version.
version = ".".join(release.split(".")[:2])

pygments_style = "sphinx"

html_theme = "sphinx_rtd_theme"

# html_theme_options = {}

html_static_path = ["_static"]

htmlhelp_basename = "drf-auth-doc"


intersphinx_mapping = {
    "python": ("https://docs.python.org/3.8", None),
}

# -- Doctest configuration ----------------------------------------

import doctest

doctest_default_flags = (
    0
    | doctest.DONT_ACCEPT_TRUE_FOR_1
    | doctest.ELLIPSIS
    | doctest.IGNORE_EXCEPTION_DETAIL
    | doctest.NORMALIZE_WHITESPACE
)