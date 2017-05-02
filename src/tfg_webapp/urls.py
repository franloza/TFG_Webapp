from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.cache import never_cache
from termsandconditions.decorators import terms_required

import profiles.urls
import accounts.urls
from . import views

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^users/', include(profiles.urls, namespace='profiles')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^report/$', never_cache(terms_required(views.ReportPage.as_view())), name='report'),
    url(r'^delete_datafile/(?P<pk>\d+)/$', views.ReportPage.delete_datafile, name='delete_datafile'),
    url(r'^', include(accounts.urls, namespace='accounts')),
    url(r'^terms/', include('termsandconditions.urls')),
]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Include django debug toolbar if DEBUG is on
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
