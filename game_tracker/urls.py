from django.urls import path
from game_tracker import views

app_name = "game_tracker"
urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("profile/<str:str>/", views.ProfileDetail.as_view(), name="profile-detail"),
    path("game-library/", views.GameLibraryList.as_view(), name="game-library-list"),
    path("community/", views.CommunityHomeList.as_view(), name="community-home-list"),
    path("community/<str:str>/", views.CommunityGameDetail.as_view(), name="community-game-detail"),
    path("game/<slug:slug>/", views.GameDetail.as_view(), name="game-detail"),
    path("profle/<str:str>/stats/", views.ProfileStatsDetail.as_view(), name="stats-detail"),
]