from django import template


register = template.Library()

def price(liveData,code):
    return float(liveData[code])

register.filter('price',price)