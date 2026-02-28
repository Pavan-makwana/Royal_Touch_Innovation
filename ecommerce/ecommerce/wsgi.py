import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')

# Pehle application define karo
application = get_wsgi_application()

# Phir Vercel ke liye usse 'app' variable mein assign karo
app = application