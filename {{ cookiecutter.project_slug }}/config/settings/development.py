from config import settings


class Development(settings.Base):
    env = settings.Base.env

    # http://whitenoise.evans.io/en/latest/django.html#using-whitenoise-in-development
    INSTALLED_APPS = ["whitenoise.runserver_nostatic"] + settings.Base.INSTALLED_APPS
