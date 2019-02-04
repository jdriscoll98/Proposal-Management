from .base import *

SECRET_KEY = 'xH8C6GEsGiYZXRb9NjKFfysi1jNhAUKpuBnj2nABsGjPhCChM2'

DEBUG = True

ALLOWED_HOSTS = ['*']

# Email Backend

EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'TMProposalManagement@gmail.com'
# EMAIL_HOST_PASSWORD = 'pmrnxnquevxjbdvp'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True

# Google ReCaptcha

RECAPTCHA_SECRET_KEY = '6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe'

RECAPTCHA_SITE_KEY = '6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI'
