import requests
from background_task import background

from setup.settings import DEFAULT_FROM_EMAIL
from .models import Asset, PriceHistory
from django.core.mail import send_mail

def getAllAssets():
    try:
        url = 'https://brapi.dev/api/quote/list?sortBy=name&sortOrder=asc'
        response_allasset = requests.get(url)
        list_assets = response_allasset.json()
        
        mapped_assets = []
        for asset in list_assets['stocks']:
            mapped_asset = {
                'asset': asset['stock'],
                'name': asset['name'],
                'change': asset['change'],
                'close': asset['close'],
                'logo': asset['logo']
            }
            mapped_assets.append(mapped_asset)

        return mapped_assets

    except:
        raise Exception("Erro ao obter a lista de ativos")

def getAsset(asset_code):
    try:
        url = 'https://brapi.dev/api/quote/%s' %asset_code
        response_asset = requests.get(url)
        asset_result = response_asset.json()['results'][0]
        
        asset = {
                'symbol': asset_result['symbol'],
                'longName': asset_result['longName'],
                'currency' : asset_result['currency'],
                'regularMarketPrice': asset_result['regularMarketPrice'],
                'regularMarketChangePercent': asset_result['regularMarketChangePercent'],
                'regularMarketTime': asset_result['regularMarketTime']
            }
        
        return asset
        
    except:
        raise Exception("Erro ao obter a lista de ativos")
 
@background(schedule=0)   
def getAssetPrice(code):
    
    asset = Asset.objects.get(asset_code = code)
    
    url = 'https://brapi.dev/api/quote/%s' %asset.asset_code
    request = requests.get(url)
    asset_price = request.json()
    
    price_history = PriceHistory(asset_code = asset.asset_code, price = asset_price['results'][0]['regularMarketPrice'], update_time = asset_price['results'][0]['regularMarketTime'], asset = asset)
    price_history.save()
    
    if price_history.price >= asset.tunel_max:
        message = f'O ativo {asset.asset_code} pode ser vendido\nValor configurado: R$ {asset.tunel_max}\nCotação: R$ {price_history.price}'
        send_mail(
            subject = 'Seu ativo pode ser vendido',
            message = message,
            recipient_list = [asset.email],
            from_email = DEFAULT_FROM_EMAIL,
            fail_silently = False
        )
        
    if price_history.price <= asset.tunel_min:
        message = f'O ativo {asset.asset_code} pode ser comprado\nValor configurado: R$ {asset.tunel_min}\nCotação: R$ {price_history.price}'
        send_mail(
            subject = 'Seu ativo pode ser comprado',
            message = message,
            recipient_list = [asset.email],
            from_email = DEFAULT_FROM_EMAIL,
            fail_silently = False
        )
    
    return None

def getAssetList():
    
    return list(Asset.objects.all())