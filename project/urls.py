
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
admin.site.site_header = 'Books Store Admin'
admin.site.site_title = 'Books Store Admin'
admin.site.index_title = 'Books Store Administration'

urlpatterns = i18n_patterns(
    path('accounts/', include('allauth.urls')),

    path('admin/', admin.site.urls),
    path('', include('Books.urls', namespace='Books')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
