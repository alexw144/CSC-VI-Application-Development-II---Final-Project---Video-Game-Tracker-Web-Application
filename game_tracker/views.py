from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView
from .models import Profile

# Create your views here.
class Index(View):
    template_name = "game_tracker/index.html"

    def get(self, request):
        return render(request, self.template_name)

class ProfileDetail(DetailView):
    model = Profile
    template_name = "game_tracker/gametrackerprofile.html"

    def get_object(self):
        if Profile.objects.filter(user=self.request.user):
            return self.model.objects.get(user=self.request.user)
        else:
            Profile.objects.create(user=self.request.user)
            return self.model.objects.get(user=self.request.user)


class GameLibraryList(ListView):
    model = ""
    template_name = ""


class CommunityHomeList(ListView):
    model = ""
    template_name = ""


class CommunityGameDetail(DetailView):
    model = ""
    template_name = ""


class GameDetail(DetailView):
    model = ""
    template_name = ""


class ProfileStatsDetail(DetailView): 
    model = ""
    template_name = ""
