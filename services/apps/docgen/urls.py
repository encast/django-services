# django
from django.urls import re_path
from django.contrib import admin
# services

# app
from services.apps.docgen.controllers import DocController
admin.autodiscover()

urlpatterns = [
    re_path(r'', DocController()),
]
