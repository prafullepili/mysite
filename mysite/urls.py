from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('', TemplateView.as_view(template_name='home/main.html')),
    path('',include('WxPortfolio.urls',namespace='wx')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),

    # path('autos/', include('autos.urls')),
    # path('polls/', include('polls.urls')),
    # path('hello/', include('hello.urls')),
    # path('cats/',include('cats.urls',namespace='cats')),
    # path('ads/',include('ads.urls')),
    # path('barns/',include('barns.urls',namespace='barns')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
