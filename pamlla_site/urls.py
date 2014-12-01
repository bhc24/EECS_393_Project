from django.conf.urls import patterns, include, url
from django.contrib import admin
from pamlla import views


admin.autodiscover()

#TODO: Pass patient arguments
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pamlla_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^patient_list/', views.patients),
    url(r'^add_patient/', views.add_patient),
    url(r'^login/', views.login_view),
    url(r'^home/', views.patients),
    url(r'^history/', views.history),
    url(r'^signup/', views.register),
    url(r'^logout/', views.logout_view),
    url(r'^$', views.login_view)
)
