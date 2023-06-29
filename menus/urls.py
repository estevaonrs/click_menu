from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (GeralMenu, MenuCreate, MenuDelete, MenuNameCreate,
                    MenuNameDelete, MenuUpdate, QrCode, SeeMenuName,
                    post_detail, public_menu)

app_name = 'menus'

urlpatterns = [
    path('', GeralMenu, name="menus"),
    path('MenuCreate/', MenuCreate.as_view(),
         name='create_menu'),
    path('MenuEdit/<int:pk>/', MenuUpdate.as_view(),
         name='update_menu'),
    path('MenuDelete/<int:pk>/', MenuDelete.as_view(),
         name='delete_menu'),
    path('MenuNameCreate/', MenuNameCreate.as_view(),
         name='create_menuname'),
    path('<slug:slug>', post_detail, name='post_detail'),
    path('SeeMenuName/', SeeMenuName, name='see_menuname'),
    path('MenuNameDelete/<slug:slug>/', MenuNameDelete.as_view(),
         name='delete_menuname'),
    path('public_menu/<slug:slug>/', public_menu, name='public_menu'),
    path('QrCode/', QrCode,
         name='qrcode'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
