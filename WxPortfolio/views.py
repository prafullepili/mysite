from django.shortcuts import render
from .models import Coins
from scripts.script import getLiveData

appName = 'WxPortfolio'
def index(request):
    live = getLiveData()
    liveData = dict(live.T['last'])
    allCoins = Coins.objects.all()
    context = {'allCoins':allCoins,"liveData":liveData}
    return render(request,f"{appName}/home.html",context)

def AddRecord(request,code):
    return render(request,f"{appName}/addRecord.html", {"code":code})