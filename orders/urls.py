from django.urls import path

from .views import (GeralOrders, OrdersCreate, OrdersDelete, OrdersList,
                    OrdersUpdate)

app_name = 'orders'

urlpatterns = [
    path('', GeralOrders,
         name="create_orders"),
    path('OrdersCreate/', OrdersCreate.as_view(),
         name="create_orders"),
    path('OrdersList/', OrdersList.as_view(),
         name='list_orders'),
    path('OrdersEdit/<int:pk>/', OrdersUpdate.as_view(),
         name='update_orders'),
    path('OrdersDelete/<int:pk>/', OrdersDelete.as_view(),
         name='delete_orders'),
]
