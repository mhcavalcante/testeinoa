from django.urls import path
from testeinoa.views import index

urlpatterns = [
    path('', index),
]

