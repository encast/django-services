

from django.urls import re_path
from controllers import AliveController

urlpatterns = [re_path(r'^alive/?', AliveController()),

               ]
