from django.shortcuts import render

from django.views.generic import TemplateView

class HomePageView(TemplateView):
  template_name ='home.html'

class AboutPageView(TemplateView):
  template_name='about.html'

class ClubPageView(TemplateView):
  template_name='club.html'

class InfoPageView(TemplateView):
  template_name='info.html'
# Create your views here.
