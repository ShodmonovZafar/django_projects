from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class ExampleView(TemplateView):
    template_name = 'example.html'
    pass
