from django.views import generic
from .models import YourResolutions
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class IndexView(generic.ListView):
    template_name = 'resolution/index.html'

    def get_queryset(self):
        return YourResolutions.objects.all()


class DetailView(generic.DetailView):
    model = YourResolutions
    template_name = 'resolution/detail.html'



class ResolutionCreate(CreateView):
    model = YourResolutions
    fields = ['resolution_title', 'resolution_category', 'resolution_year']


class ResolutionUpdate(UpdateView):
    model = YourResolutions
    fields = ['resolution_title', 'resolution_category', 'resolution_year']


class ResolutionDelete(DeleteView):
    model = YourResolutions
    success_url = reverse_lazy('resolution:index')
