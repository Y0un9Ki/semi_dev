from django.urls import path
from users.views import signin_view, signout_view, signup_view

urlpatterns = [
    path('signin/', signin_view),
    path('signout/', signout_view),
    path('signup/', signup_view),
]
