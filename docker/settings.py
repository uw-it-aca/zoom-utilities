from .base_settings import *

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
                # "zoom_utilities.context_processors.auth_user",
            ],
        },
    }
]


if os.getenv("ENV") == "localdev":
    DEBUG = True

if os.getenv("ENV") == "localdev":
    VITE_MANIFEST_PATH = os.path.join(
        BASE_DIR, "zoom_utilities", "static", "manifest.json"
    )
else:
    VITE_MANIFEST_PATH = os.path.join(os.sep, "static", "manifest.json")
