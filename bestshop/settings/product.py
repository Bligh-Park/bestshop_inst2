from .base import *


DEBUG=False

INSTALLED_APPS += [
    'raven.contrib.django.raven_compat'
]

import os
import raven

RAVEN_CONFIG = {
    'dsn': 'https://2294579be6f24a4eaba276fdcae411b7:2a41de4bfc2948aaa2af72e22612c165@sentry.io/160714',
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    'release': raven.fetch_git_sha(os.path.dirname(os.pardir)),
}


# SMTP Username:
# AKIAJLOLA3RFHAYSZ2WQ
# SMTP Password:
# AuANfJWzyYKL+O1CkcJ9zayVIroeeUDiD8QIHAx91CaE

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'email-smtp.us-west-2.amazonaws.com'
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'AKIAJLOLA3RFHAYSZ2WQ'
EMAIL_HOST_PASSWORD = 'AuANfJWzyYKL+O1CkcJ9zayVIroeeUDiD8QIHAx91CaE'