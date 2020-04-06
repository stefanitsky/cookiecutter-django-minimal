import configurations
import environ


class Base(configurations.Configuration):
    # Path configurations
    # /{{ cookiecutter.project_slug }}/settings/base.py - 3
    ROOT_DIR = environ.Path(__file__) - 3
    APPS_DIR = ROOT_DIR / "{{ cookiecutter.project_slug }}"

    # Environment
    env = environ.Env()

    # General
    # ------------------------------------------------------------------------------
    # https://docs.djangoproject.com/en/dev/ref/settings/#debug
    DEBUG = env.bool("DJANGO_DEBUG", default=False)
    SECRET_KEY = env("DJANGO_SECRET_KEY")
    # Local time zone. Choices are
    # http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
    # though not all of them may be available with every OS.
    # In Windows, this must be set to your system time zone.
    TIME_ZONE = "{{ cookiecutter.timezone }}"
    # https://docs.djangoproject.com/en/dev/ref/settings/#language-code
    LANGUAGE_CODE = "en-us"
    # https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
    USE_I18N = True
    # https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
    USE_L10N = True
    # https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
    USE_TZ = True
    # https://docs.djangoproject.com/en/dev/ref/settings/#locale-paths
    LOCALE_PATHS = [str(ROOT_DIR / "locale")]
    ALLOWED_HOSTS = env("DJANGO_ALLOWED_HOSTS", default=["*"])
    # https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
    ROOT_URLCONF = '{{ cookiecutter.project_slug }}.urls'
    # https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
    WSGI_APPLICATION = '{{ cookiecutter.project_slug }}.wsgi.application'
    # Custom admin url
    ADMIN_URL = env("DJANGO_ADMIN_URL", default="admin/")

    # Applications
    # ------------------------------------------------------------------------------
    DJANGO_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
    ]
    THIRD_PARTY_APPS = []
    LOCAL_APPS = []
    # https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
    INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

    # Middleware
    # ------------------------------------------------------------------------------
    # https://docs.djangoproject.com/en/dev/ref/settings/#middleware
    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "whitenoise.middleware.WhiteNoiseMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]

    # Templates
    # ------------------------------------------------------------------------------
    TEMPLATES = [
        {
            # https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                # https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
                # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
                "loaders": [
                    "django.template.loaders.filesystem.Loader",
                    "django.template.loaders.app_directories.Loader",
                ],
                # https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
                'context_processors': [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.template.context_processors.i18n",
                    "django.template.context_processors.media",
                    "django.template.context_processors.static",
                    "django.template.context_processors.tz",
                    "django.contrib.messages.context_processors.messages",
                ],
            },
        },
    ]

    # Databases
    # ------------------------------------------------------------------------------
    # https://docs.djangoproject.com/en/dev/ref/settings/#databases
    DATABASES = {"default": env.db("DATABASE_URL")}
    DATABASES["default"]["ATOMIC_REQUESTS"] = True

    # Authentication
    # https://docs.djangoproject.com/en/dev/ref/settings/#authentication-backends
    AUTHENTICATION_BACKENDS = [
        "django.contrib.auth.backends.ModelBackend",
        "allauth.account.auth_backends.AuthenticationBackend",
    ]

    # Passwords
    # ------------------------------------------------------------------------------
    # https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
    PASSWORD_HASHERS = [
        # https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
        "django.contrib.auth.hashers.Argon2PasswordHasher",
        "django.contrib.auth.hashers.PBKDF2PasswordHasher",
        "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
        "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    ]
    # https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
    AUTH_PASSWORD_VALIDATORS = [
        {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
        {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
        {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
        {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
    ]

    # Staticfiles
    # ------------------------------------------------------------------------------
    # https://docs.djangoproject.com/en/dev/ref/settings/#static-root
    STATIC_ROOT = str(ROOT_DIR / "staticfiles")
    # https://docs.djangoproject.com/en/dev/ref/settings/#static-url
    STATIC_URL = "/static/"
    STATICFILES_DIRS = [str(APPS_DIR / "static")]
    # https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
    STATICFILES_FINDERS = [
        "django.contrib.staticfiles.finders.FileSystemFinder",
        "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    ]

    # Media
    # ------------------------------------------------------------------------------
    # https://docs.djangoproject.com/en/dev/ref/settings/#media-root
    MEDIA_ROOT = str(APPS_DIR / "media")
    # https://docs.djangoproject.com/en/dev/ref/settings/#media-url
    MEDIA_URL = "/media/"

    # Fixtures
    # ------------------------------------------------------------------------------
    # https://docs.djangoproject.com/en/dev/ref/settings/#fixture-dirs
    FIXTURE_DIRS = [str(APPS_DIR / "fixtures")]

    # Security
    # ------------------------------------------------------------------------------
    # https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-httponly
    CSRF_COOKIE_HTTPONLY = True
    # https://docs.djangoproject.com/en/dev/ref/settings/#secure-browser-xss-filter
    SECURE_BROWSER_XSS_FILTER = True
