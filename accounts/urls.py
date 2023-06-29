from django.contrib.auth import views as auth_views
from django.urls import path

from .classes import (password_reset, password_reset_complete,
                      password_reset_confirm, password_reset_done)
from .views import (AccountsCreate, AccountsList, AccountsUpdate,
                    GeralAccounts, PasswordChange, logout)

app_name = 'accounts'

urlpatterns = [
    path('', GeralAccounts, name='GeralAccounts'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('logout/', logout, name='logout'),
    path('AccountsCreate/', AccountsCreate.as_view(), name='create_accounts'),
    path('AccountsUpdate/', AccountsUpdate.as_view(), name='update_accounts'),
    path('AccountsList/', AccountsList.as_view(), name='list_accounts'),
    path('PasswordChange/', PasswordChange, name='change_password'),
    path('resetPassword/', password_reset, name='resetPassword'),
    path('resetPassword/password_reset_done/',
         password_reset_done, name='password_reset_done'),
    path('reset/<uid64>/<token>/', password_reset_confirm,
         name='password_reset_confirm'),
    path('reset/done/', password_reset_complete,
         name='password_reset_complete'),
]
