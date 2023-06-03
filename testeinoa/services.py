import requests

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
                'regularMarketChangePercent': asset_result['regularMarketChangePercent']
            }
        
        return asset
        
    except:
        raise Exception("Erro ao obter a lista de ativos")