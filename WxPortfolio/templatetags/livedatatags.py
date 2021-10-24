from django import template
# from WxPortfolio.models import Coins
from scripts.script import getLiveData


register = template.Library()

def price(liveData,code):
    return liveData[code]

register.filter('price',price)