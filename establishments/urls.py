from django.urls import path

from .views import (EstablishmentCreate, EstablishmentDelete,
                    EstablishmentList, EstablishmentUpdate,
                    GeralEstablishments)

app_name = 'establishments'

urlpatterns = [
    path('', GeralEstablishments,
         name="GeralEstablishments"),
    path('EstablishmentCreate/', EstablishmentCreate.as_view(),
         name='create_establishment'),
    path('EstablishmentList/', EstablishmentList.as_view(),
         name='list_establishment'),
    path('EstablishmentEdit/<int:pk>/', EstablishmentUpdate.as_view(),
         name='update_establishment'),
    path('EstablishmentDelete/<int:pk>/', EstablishmentDelete.as_view(),
         name='delete_establishment'),
]
