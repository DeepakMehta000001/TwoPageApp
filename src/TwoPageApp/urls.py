from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static


urlpatterns = [
    # Examples:
    url(r'^$', 'records.views.showRecords', name='showRecords'),
    url(r'^home/$', 'records.views.showRecords', name='showRecords'),
    url(r'^add/$', 'records.views.add', name='add'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
