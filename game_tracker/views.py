from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView
from .models import Profile
import json
from django.http import JsonResponse

# Create your views here.
# This is the view that connects to the homepage
class Index(View):
    template_name = "game_tracker/index.html"

    def get(self, request):
        return render(request, self.template_name)


# This is the view that coonects to the users Profile page
class ProfileDetail(DetailView):
    model = Profile
    template_name = "game_tracker/gametrackerprofile.html"

    # This function checks if the logged in user has a profile.
    # If the user has a profile, the profile is returned. 
    def get_object(self):
        if Profile.objects.filter(user=self.request.user):
            return self.model.objects.get(user=self.request.user)
        else: # if there is no profile connected to the user, a profile is created based from the user.
            Profile.objects.create(user=self.request.user)
            return self.model.objects.get(user=self.request.user)
    
    # This function is for updating the users profile and information. This function can edited in the future to change the things the user can update.
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        profile = self.get_object()

        # Update Section
        profile.birthday = data.get('birthday', profile.birthday)
        profile.gender = data.get('gender', profile.gender)
        profile.user.username = data.get('username', profile.user.username)
        profile.user.email = data.get('email', profile.user.email)
        
        profile.user.save()
        profile.save()
        return JsonResponse({'status': 'success'})
        

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
