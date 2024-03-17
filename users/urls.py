from django.urls import path
from users.views import signin_view

urlpatterns = [
    path('signin/', signin_view)
]
