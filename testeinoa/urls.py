from . import views
from django.urls import path
from testeinoa.models import Asset
from testeinoa.views import index

urlpatterns = [
    path('', views.index, name='index'),
    
    path('assets', views.listAssets, name='assets'),
]

