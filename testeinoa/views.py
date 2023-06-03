from django.shortcuts import render
from django.http import HttpResponse

from testeinoa.services import getAllAssets, getAsset

def index(request):
    ##list_stocks = getAllStocks()
    ##print(list_stocks)
    
    stock = getAsset('MGLU3')
    print(stock['longName'])
    
    return render(request, 'testeinoa/index.html')
    