import {{ cookiecutter.project_slug }}
from config import settings


class Production(settings.Base):
    env = settings.Base.env

    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

    # SSL: https://docs.djangoproject.com/en/dev/topics/security/#ssl-https
    SECURE_SSL_REDIRECT = env("DJANGO_SECURE_SSL_REDIRECT", default=False)
    SECURE_HSTS_SECONDS = 60
    SECURE_HSTS_PRELOAD = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

    # Sentry
    SENTRY_SEND_DEFAULT_PII = True
    SENTRY_RELEASE = "{{ cookiecutter.project_slug }}@{version}".format(version={{ cookiecutter.project_slug }}.__version__)
    SENTRY_ENVIRONMENT = "production"
    SENTRY_DEBUG = False

    def __init__(self, *args, **kwargs):
        super().__init__()
        import sentry_sdk
        sentry_sdk.init(
            dsn=self.env("SENTRY_DSN"),
            integrations=[sentry_sdk.integrations.django.DjangoIntegration()],
            send_default_pii=self.SENTRY_SEND_DEFAULT_PII,
            release=self.SENTRY_RELEASE,
            environment=self.SENTRY_ENVIRONMENT,
            debug=self.SENTRY_DEBUG,
        )
