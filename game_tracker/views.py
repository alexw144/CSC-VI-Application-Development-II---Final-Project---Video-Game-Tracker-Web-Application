from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView
from .models import Profile, Game, Review, UsersGamesStat, Review, Post, PostComment
import json
from django.http import JsonResponse
from datetime import timedelta


# Create your views here.
# This is the view that connects to the homepage
class Index(View):
    template_name = "game_tracker/index.html"

    def get(self, request):
        return render(request, self.template_name)


# This is the view that connects to the users Profile page
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
        

# This is the view that connects to the Game Library. It displays all the games.
class GameLibraryList(ListView):
    model = Game
    template_name = "game_tracker/gamelibrarylist.html"


# This is the view that connects to a specific game page. It displays all the information about the game.
class GameDetail(DetailView):
    model = Game
    template_name = "game_tracker/gamedetail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = self.add_reviews_to_context(context)
        context = self.add_user_stats_to_context(context)
        return context
    
    def add_reviews_to_context(self, context):
        game = self.get_object()
        reviews = Review.objects.filter(game=game)
        context['reviews'] = reviews
        return context
    
    def add_user_stats_to_context(self, context):
        game = self.get_object()
        user_stats = UsersGamesStat.objects.filter(game=game, user=self.request.user).first()
        context['user_stats'] = user_stats
        return context
    
    # This function is for posting CRUDs to the dataabse. Specifcally ones relateted to Game Detail page.
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        game = self.get_object()
        action = data.get('action')

        # determines which POST request and directs as needed
        if action == 'update_user_game_stats':
            return self.update_user_game_stats(request, game, data)
        elif action == 'submit_user_review':
            return self.submit_user_review(request, game, data)
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid action'}, status=400)

    # This function is for updating the users game stats for a specific game or creating new stats.
    def update_user_game_stats(self, request, game, data): 
        try:
        # Try to get the existing userStats record
            userStats = UsersGamesStat.objects.get(game=game, user=request.user)
        except UsersGamesStat.DoesNotExist:
        # If it doesn't exist, create a new one
            userStats = UsersGamesStat.objects.create(
                game=game,
                user=request.user,
                time_played=timedelta(),
                date_first_played=None,
                date_last_played=None,
                date_beaten=None,
                status='',
                user_rating=0,
                progress_percentage=0,
                achievement_count=0,
                notes=''
            )

        time_played_decimal = data.get('time', 0)
        
        # Convert decimal hours into timedelta
        hours = int(time_played_decimal)  # The whole number is the hours
        minutes = int((time_played_decimal - hours) * 60)  # Convert the fraction into minutes
        time_played_timedelta = timedelta(hours=hours, minutes=minutes)

        # Update Section
        userStats.time_played = time_played_timedelta
        userStats.date_first_played = data.get('first', userStats.date_first_played)
        userStats.date_last_played = data.get('last', userStats.date_last_played)
        userStats.date_beaten = data.get('beaten', userStats.date_beaten)
        userStats.status = data.get('status', userStats.status)
        userStats.user_rating = data.get('rating', userStats.user_rating)
        userStats.progress_percentage = data.get('percent', userStats.progress_percentage)
        userStats.achievement_count = data.get('achievement', userStats.achievement_count)
        userStats.notes = data.get('notes',  userStats.notes)
        
        userStats.save()
        return JsonResponse({'status': 'success'})
    
    # This function is for updating the users game stats for a specific game or creating new stats.
    def submit_user_review(self, request, game, data):
        try:
            # Try to get an existing review by the user for this game
            review = Review.objects.get(game=game, user=request.user)
        except Review.DoesNotExist:
            # If no review exists, create a new one
            review = Review.objects.create(
                game=game,
                user=request.user,
                review_title=data.get('title', ''),  # Default to empty string if not provided
                review_body=data.get('review', '')  # Default to empty string if not provided
            )
        
        # Create the review
        review.review_title = data.get('title', review.review_title)
        review.review_body = data.get('review', review.review_body)
        review.save()

        return JsonResponse({'status': 'success'})


class CommunityHomeList(ListView):
    model = Post
    template_name = "game_tracker/communitylist.html"


class CommunityGameDetail(DetailView):
    model = ""
    template_name = ""


class ProfileStatsDetail(DetailView): 
    model = ""
    template_name = ""
