from django.urls import patterns, include, re_path
from services.apps.ops.controllers import StatusController, DeployController, HealthController, ErrorReportController
urlpatterns = patterns('',
                       re_path(r'^status/?$', StatusController()),
                       re_path(r'^health/?$', HealthController()),
                       re_path(r'^deploy/?$', DeployController()),
                       re_path(r'^error/?$', ErrorReportController()),
                       )
