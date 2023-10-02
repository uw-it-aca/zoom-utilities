from .base_settings import *
from google.oauth2 import service_account
import os

INSTALLED_APPS += [
    "zoom_utilities.apps.ZoomUtilitiesConfig",
]

# If you have file data, define the path here
# DATA_ROOT = os.path.join(BASE_DIR, "zoom_utilities/data")

GOOGLE_ANALYTICS_KEY = os.getenv("GOOGLE_ANALYTICS_KEY", default=" ")

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "debug": True,
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "zoom_utilities.context_processors.google_analytics",
                "zoom_utilities.context_processors.django_debug",
                "zoom_utilities.context_processors.auth_user",
            ],
        },
    }
]

if os.getenv("ENV", "localdev") == "localdev":
    DEBUG = True
    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
    MEDIA_ROOT = os.getenv('MEDIA_ROOT', '/app/data')
    VITE_MANIFEST_PATH = os.path.join(
        BASE_DIR, "zoom_utilities", "static", "manifest.json"
    )
else:
    VITE_MANIFEST_PATH = os.path.join(os.sep, "static", "manifest.json")
    DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
    GS_PROJECT_ID = os.getenv('STORAGE_PROJECT_ID', '')
    GS_BUCKET_NAME = os.getenv('STORAGE_BUCKET_NAME', '')
    GS_LOCATION = os.path.join(os.getenv('STORAGE_DATA_ROOT', ''))
    GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
        '/gcs/credentials.json')
    CSRF_TRUSTED_ORIGINS = ['https://' + os.getenv('CLUSTER_CNAME')]
