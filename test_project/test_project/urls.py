from django.urls import patterns, include, re_path

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from main.controllers import *
from services.apps.docgen import urls as docgen_urls

urlpatterns = patterns('',
    # Examples:
     re_path(r'^crud/?$', CRUDController()),
     re_path(r'^blog/?$', BlogPostController()),
     re_path(r'^blog/(?P<blog_id>[\d]+)/?$', BlogPostController()),
     re_path(r'^', include(docgen_urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
