from django.contrib.auth.views import (LoginView, PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView,
                                       PasswordChangeView)
from django.urls import path, reverse_lazy
from store import views as store_views

from authorization import views

urlpatterns = [
    path(
        'login/',
        LoginView.as_view(
            template_name='sign_in.html',
            next_page='my_rent'
        ),
        name="sign_in"
    ),
    path('register/', views.register, name='sign_up'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('change_password/', views.change_password, name='change_password'),
]