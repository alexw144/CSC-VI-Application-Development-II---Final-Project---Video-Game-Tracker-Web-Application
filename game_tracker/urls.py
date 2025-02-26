from django.urls import path
from game_tracker import views

app_name = "sleeptracker"
urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("profile/", views.ProfileDetail.as_view(), name="profile-detail"),
    path("game-library/", views.GameLibraryList.as_view(), name="game-library-list"),
    path("community/", views.CommunityList.as_view(), name="community-list"),
    path("game-library/<str:str>/", views.LogsDetail.as_view(), name="game-detail"),
    path("profle/stats/", views.ProfileStatsDetail.as_view(), name="stats-detail"),
]