from . import views
from django.urls import path
from testeinoa.models import Asset
from testeinoa.views import index

urlpatterns = [
    path('', views.index, name='index'),
    
    path('assets', views.listAssets, name='assets'),
    path('assets/add', views.addAsset, name='addAsset'),
    path('assets/history/<str:asset_code>', views.priceHistory, name='priceHistory'),
    path('assets/delete/<str:asset_code>', views.deleteAsset, name='deleteAsset'),
]

