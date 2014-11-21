from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from pamlla.views import patients, add_patient, login, home, history

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pamlla_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^patients/', patients),
    url(r'^add_patient/', add_patient),
    url(r'^login/', login),
    url(r'^home/', home),
    url(r'^history/', history)
)
