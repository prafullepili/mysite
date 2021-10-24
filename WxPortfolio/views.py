from django.shortcuts import render
from .models import Coins
from scripts.script import getLiveData

def index(request):
    live = getLiveData()
    liveData = dict(live.T['last'])
    allCoins = Coins.objects.all()
    context = {'allCoins':allCoins,"liveData":liveData}
    return render(request,"WxPortfolio/home.html",context)