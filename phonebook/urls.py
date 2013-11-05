from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'phonebook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', 'phonebook.views.Login'),
    url(r'^contact/', 'phonebook.views.Contact'),
    url(r'^addcontact/$','phonebook.views.AddContact'),
    url(r'^logout/', 'phonebook.views.Logout'),
)
