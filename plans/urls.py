from django.urls import path

from .views import GeralPlans, plano_detail


app_name = 'plans'

urlpatterns = [
    path('', GeralPlans, name="GeralPlans"),
    path('plano/<int:plano_id>/', plano_detail, name='plano_detail'),


]
