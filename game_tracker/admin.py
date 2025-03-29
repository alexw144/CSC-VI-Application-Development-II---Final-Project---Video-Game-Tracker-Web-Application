from django.contrib import admin
from .models import Profile, Game, UsersGamesStat, Review, Post, PostComment

# Register your models here.
admin.site.register(Profile)
admin.site.register(Game)
admin.site.register(UsersGamesStat)
admin.site.register(Review)
admin.site.register(Post)
admin.site.register(PostComment)
