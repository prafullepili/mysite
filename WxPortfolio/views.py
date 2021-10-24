from django.shortcuts import render
from django.template import context
from .models import Coins
from scripts.script import getLiveData

def index(request):
    live = getLiveData()
    allCoins = Coins.objects.all()
    liveData = dict(live.T['last'])
    context = {'allCoins':allCoins, "liveData":liveData}
    return render(request,"WxPortfolio/home.html",context)