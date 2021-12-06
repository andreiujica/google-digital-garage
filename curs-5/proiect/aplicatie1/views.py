from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, ListView

from aplicatie1.models import Location


# Create your views here.
class CreateLocationView(CreateView):
    model = Location
    fields = ['city', 'country']
    template_name = 'aplicatie1/location_form.html'

    def get_success_url(self):
        return reverse('aplicatie1:listare')


class UpdateLocationView(UpdateView):
    model = Location
    fields = ['city', 'country']
    template_name = 'aplicatie1/location_form.html'

    def get_success_url(self):
        return reverse('aplicatie1:listare')


class ListLocationView(ListView):
    model = Location
    template_name = 'aplicatie1/location_index.html'

