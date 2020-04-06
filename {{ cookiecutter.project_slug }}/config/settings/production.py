from config import settings


class Production(settings.Base):
    env = settings.Base.env

    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
