from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('meineadmin/', admin.site.urls),
    path('', include('authen.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Dbaba Admin"
admin.site.site_title = "Dbaba Admin Portal"
admin.site.index_title = "Welcome to Dbaba Blog Portal"

