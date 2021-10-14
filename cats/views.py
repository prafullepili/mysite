from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from cats.models import Breed
from cats.models import Cat
from cats.forms import BreedForm


# path('',views.CatList.as_view(), name='all'),
class CatList(LoginRequiredMixin, View):
    def get(self, request):
        breed_count = Breed.objects.all().count()
        cat_list = Cat.objects.all()
        ctx = {'breed_count': breed_count, 'cat_list': cat_list}
        return render(request, 'cats/cat_list.html', ctx)


# path('lookup/create/', views.BreedCreate.as_view(), name='breed_create'),
class BreedCreate(LoginRequiredMixin, View):
    template = 'cats/breedCreate_form.html'
    success_url = reverse_lazy('cats:all')

    def get(self, request):
        form = BreedForm()
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request):
        form = BreedForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)
        form.save()
        return redirect(self.success_url)


# path('lookup/', views.BreedView.as_view(), name='breed_list'),
class BreedView(LoginRequiredMixin, View):
    def get(self, request):
        breed_list = Breed.objects.all()
        ctx = {'breed_list': breed_list}
        return render(request, 'cats/breed_list.html', ctx)    


# path('main/create/',views.CatCreate.as_view(), name='cat_create'),
class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')


# path('main/<int:pk>/update/',views.CatUpdate.as_view(), name='cat_update'),
class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

# path('main/<int:pk>/delete/', views.CatDelete.as_view(), name='cat_delete')
class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

# path('lookup/<int:pk>/update/', views.BreedUpdate.as_view(), name='breed_update'),
class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    template_name = 'cats/breedCreate_form.html'
    success_url = reverse_lazy('cats:all')

# path('lookup/<int:pk>/delete/', views.BreedDelete.as_view(), name='breed_delete'),
class BreedDelete(LoginRequiredMixin, DeleteView):
    template_name = 'cats/cat_confirm_delete.html'
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

# class MakeDelete(LoginRequiredMixin, View):
#     model = Make
#     success_url = reverse_lazy('autos:all')
#     template = 'autos/make_confirm_delete.html'

#     def get(self, request, pk):
#         make = get_object_or_404(self.model, pk=pk)
#         form = MakeForm(instance=make)
#         ctx = {'make': make, 'form':form}
#         return render(request, self.template, ctx)

#     def post(self, request, pk):
#         make = get_object_or_404(self.model, pk=pk)
#         make.delete()
#         return redirect(self.success_url)



