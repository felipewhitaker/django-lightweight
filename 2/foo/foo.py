import os
import sys
from django.conf import settings

DEBUG = os.environ.get('DEBUG', 'on') == 'on'

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-kqrvfx&7y+jlqu%1x1&cik0^9$(3^*2aylve-63+pzsho0l_(g') 
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')
settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        ), 
    )

# from django.conf.urls import url
from django.conf.urls import re_path
from django.core.wsgi import get_wsgi_application 
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World')

urlpatterns = (
    re_path(r'^$', index),
)

application = get_wsgi_application()
if __name__ == "__main__":

    print(ALLOWED_HOSTS)

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)