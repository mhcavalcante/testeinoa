from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from testeinoa.forms import AssetForm
from testeinoa.models import Asset, PriceHistory
from background_task.models import CompletedTask, Task
from testeinoa.services import getAllAssets, getAsset, getAssetList, getAssetPrice

def index(request):
    return render(request, 'testeinoa/index.html')

def listAssets(request):
    listAssets = getAllAssets()
    return render(request, 'testeinoa/listAssets.html', {'listAssets': listAssets})

def addAsset(request):
    form = AssetForm(request.POST or None)
    
    if form.is_valid():
        form.clean()
        form.save()
        asset = form.cleaned_data['asset_code']
        update_frequency_sec = form.cleaned_data['update_frequency']*60
        
        getAssetPrice(asset, repeat=update_frequency_sec, repeat_until=None, verbose_name='%s' %asset)
    
    assets_list = getAssetList()
    object = {'form':form, 'assets_list':assets_list}
    
    return render(request, 'testeinoa/addAsset.html', object)

def priceHistory(request, asset_code):
    prices_list = list(PriceHistory.objects.filter(asset_code = asset_code))
    has_price = True if prices_list else False
    object = {'prices_list':prices_list, 'has_price':has_price}
    
    return render(request, 'testeinoa/priceHistory.html', object)
        
def deleteAsset(request, asset_code):
    asset = Asset.objects.get(asset_code=asset_code)
    form = AssetForm(None)
        
    asset.delete()
    assets_list = getAssetList()
    Task.objects.get(verbose_name = asset.asset_code).delete()
    CompletedTask.objects.get(verbose_name = asset.asset_code).delete()        
    
    return render(request, 'testeinoa/addAsset.html', {'form': form, 'assets_list': assets_list})

def updateAsset(request, asset_code):
    asset = Asset.objects.get(asset_code=asset_code)
    form = AssetForm(request.POST or None, instance=asset)

    if request.method == 'POST' and form.is_valid():
        form.save()
        form = AssetForm(None)
        return redirect('addAsset')

    assets_list = getAssetList()

    return render(request, 'testeinoa/addAsset.html', {'form': form, 'assets_list': assets_list})