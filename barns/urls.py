from django.urls import path
from . import views


app_name = 'barns'
urlpatterns = [ 
    path('',views.login),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('barn/',views.barn,name='barn'),
    path('barn_details/',views.barn_details,name='barns_details'),
    path('devices/',views.devices,name='devices'),

]