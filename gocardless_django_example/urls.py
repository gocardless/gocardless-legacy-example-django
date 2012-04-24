from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('gocardless_example.views',
        url(r'^$', 'index', name='home'),
        url(r'^create/bill$', 'create_bill', name='create_bill'),
        url(r'^create_subscription', 'create_subscription', name='create_subscription'),
        url(r'^create_preauth', 'create_preauth', name='create_preauth'),
        url(r'^success', 'success', name='success'),
    # Examples:
    # url(r'^$', 'gocardless_django_example.views.home', name='home'),
    # url(r'^gocardless_django_example/', include('gocardless_django_example.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
