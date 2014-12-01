from django.conf.urls import patterns, include, url
from django.contrib import admin
from pamlla.views import patients, add_patient, logout_view, login_view, home, history, register


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pamlla_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^patient_list/', patients),
    url(r'^add_patient/', add_patient),
    url(r'^login/', login_view),
    url(r'^home/', patients),
    url(r'^history/', history),
    url(r'^signup/', register),
    url(r'^logout/', logout_view),
    url(r'^$', login_view)
)
