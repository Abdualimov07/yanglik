from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404, handler500, handler403, handler400
    

urlpatterns = [
    
    path('admin/', admin.site.urls),
        
] + i18n_patterns (
    path('i18n/', include("django.conf.urls.i18n")),
    path("", include("news_app.urls")),
    path("account/", include("accounts.urls")),
) 
    
handler404 = 'news_app.views.error_404_view'
handler500 = 'news_app.views.error_500_view'
handler400 = 'news_app.views.error_400_view'
handler403 = 'news_app.views.error_403_view'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

