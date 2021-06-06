from django.urls import path
from Users.views.login import LoginFormView, LogoutRedirectView
from Users.views.create_user import UserCreateView

urlpatterns = [
    path('', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutRedirectView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='create'),
]
