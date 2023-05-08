from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True

INSTALLED_APPS: list[str] = [
    'app.apps.core',
]



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
