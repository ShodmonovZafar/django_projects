from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'html_1.html'

class AboutPageView(TemplateView):
    template_name = 'html_2.html'
