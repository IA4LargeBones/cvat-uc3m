"""
https://github.com/cvat-ai/cvat/pull/6322
"""

# Overlaying production
from cvat.settings.production import *

CSRF_TRUSTED_ORIGINS = ['https://cvat.arcos.inf.uc3m.es']

import os
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = "maxrodri@inf.uc3m.es"
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASSWORD")
DEFAULT_FROM_EMAIL = "maxrodri@inf.uc3m.es"

SITE_ID = 2
IAM_TYPE = "BASIC"
