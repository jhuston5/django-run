from django.urls import path
from .views import ClubPageView, HomePageView, AboutPageView, InfoPageView

urlpatterns = [
  path('', HomePageView.as_view(), name='home'),
  path('about', AboutPageView.as_view(), name='about'),
  path('club', ClubPageView.as_view(), name='club'),
  path('info', InfoPageView.as_view(), name='info')

]