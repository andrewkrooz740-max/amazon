"""
WSGI config for luxury_feeling_collection project.
"""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'luxury_feeling_collection.settings')
application = get_wsgi_application()
