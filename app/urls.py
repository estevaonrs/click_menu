from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('index.urls')),
    path('menus', include('menus.urls', namespace='menus')),
    path('establishment/', include('establishments.urls',
                                   namespace='establishment')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('plans/', include('plans.urls', namespace='plans')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path("admin/", admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
