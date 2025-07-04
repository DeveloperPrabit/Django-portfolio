import os
import sys

# Add your project root directory to the sys.path
sys.path.insert(0, os.path.dirname(__file__))

# Set the Django settings module environment variable
os.environ['DJANGO_SETTINGS_MODULE'] = 'webportfolio.settings'

# Import the WSGI application from your Django project
from webportfolio.wsgi import application
