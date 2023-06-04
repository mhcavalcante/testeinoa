from django.shortcuts import render
from django.http import HttpResponse

from testeinoa.services import getAllAssets, getAsset

def index(request):
    return render(request, 'testeinoa/index.html')

def listAssets(request):
    listAssets = getAllAssets()
    return render(request, 'testeinoa/listAssets.html', {'listAssets': listAssets})