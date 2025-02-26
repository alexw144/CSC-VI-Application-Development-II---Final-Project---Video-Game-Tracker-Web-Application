from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView

# Create your views here.
class Index(View):
    template_name = ""


class ProfileDetail(DetailView):
    model = ""
    template_name = ""


class GameLibraryList(ListView):
    model = ""
    template_name = ""


class CommunityList(ListView):
    model = ""
    template_name = ""


class GameDetail(DetailView):
    model = ""
    template_name = ""


class ProfileStatsDetail(DetailView): 
    model = ""
    template_name = ""
