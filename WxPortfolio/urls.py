from django.urls import path
from . import views


app_name = 'wx'
urlpatterns = [
    path('',views.index,name='home'),
    path('<str:code>/',views.AddRecord,name='addcoin'),
]