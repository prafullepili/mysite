from .owner import (
    OwnerListView, OwnerDetailView,
    OwnerCreateView,OwnerUpdateView,
    OwnerDeleteView)
from .models import Ad



class AdListView(OwnerListView):
    model = Ad

class AdDetailView(OwnerDetailView):
    model = Ad

class AdCreateView(OwnerCreateView):
    model = Ad
    fields = ['title', 'price', 'text']

class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title','price','text']

class AdDeleteView(OwnerDeleteView):
    model = Ad