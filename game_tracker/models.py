from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=15, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], blank=True, default='O')

    def __str__(self):
        return self.user.username + "'s Profile"


class Game(models.Model):
    title = models.CharField(max_length=75, blank=True)
    genre = models.CharField(max_length=50, blank=True)
    synopsis = models.TextField(default="Nothing yet, Sorry.", blank=True)
    esrb_rating = models.CharField(max_length=10, choices=[('E', 'Everyone'), ('E10', 'Everyone 10+'), ('T', 'Teen'), ('M', 'Mature 17+'), ('A', 'Adult Only 18+'), ('RP', 'Rating Pending'), ('RPM', 'Rating Pending Likely Mature 17+'), ('O', 'Other')], blank=True, default='O')
    developer = models.CharField(max_length=35, blank=True)
    publisher = models.CharField(max_length=35, blank=True)
    playstation = models.BooleanField(null=True)
    xbox = models.BooleanField(null=True)
    nintendo = models.BooleanField(null=True)
    pc = models.BooleanField(null=True)
    other = models.BooleanField(null=True)
    release_date = models.DateField(null=True, blank=True)
    game_cover_image = models.ImageField(default='fallback.png', blank=True)
    slug = models.SlugField(max_length=200, unique=False, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Game, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    

class UsersGamesStat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users_games_stats')
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    time_played = models.DurationField(default="00:00:00")
    date_first_played = models.DateField(null=True, blank=True)
    date_last_played = models.DateField(null=True, blank=True)
    date_beaten = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=[('P', 'Playing'), ('PtP', 'Plan to Play'), ('C', 'Completed'), ('B', 'Beaten'), ('H', 'On Hold'), ('W', 'Wishlist'), ('R', 'Replaying'), ('O', 'Other')], blank=True, default='O')
    user_rating = models.CharField(max_length=10, choices=[('-', 'Not Rated'),('1', 'Appalling'),('2', 'Horrible'),('3', 'Very Bad'),('4', 'Bad'),('5', 'Average'),('6', 'Fine'),('7', 'Good'),('8', 'Very Good'),('9', 'Great'),('10', 'Masterpiece')], blank=True, default='O')
    progress_percentage = models.FloatField(default=0.0)
    achievement_count = models.IntegerField(default=0)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        # Add a unique constraint to ensure one gamestat per user per game
        constraints = [
            models.UniqueConstraint(fields=['user', 'game'], name='unique_user_game_stat')
        ]

    def __str__(self):
        return self.user.username + "'s " + self.game.title + " Stats"


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_reviews')
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    review_title = models.CharField(max_length=100, blank=False)
    review_body = models.TextField(blank=False)

    class Meta:
        # Add a unique constraint to ensure one review per user per game
        constraints = [
            models.UniqueConstraint(fields=['user', 'game'], name='unique_user_game_review')
        ]

    def __str__(self):
        return self.user.username + "'s " + self.game.title + " Review"

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='posts')
    post_title = models.CharField(max_length=100, blank=False)
    post_body = models.TextField(blank=True)
    post_image = models.ImageField(blank=True, null=True, upload_to='media/posts/')
    date_added = models.DateTimeField(auto_now_add=True)
    post_type = models.CharField(max_length=10, choices=[('Art', 'Art'), ('Img', 'Image'), ('Dis', 'Discussion'), ('Evt', 'Event'), ('Gui', 'Guide'), ('Annn', 'Announcement'), ('Hel', 'Help'), ('O', 'Other')], blank=False, default='O')

    def __str__(self):
        return self.user.username + "'s " + self.game.title + " Post: " + self.post_title
    
class PostComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    post_body = models.TextField(blank=False)

    def __str__(self):
        return self.user.username + "'s Comment on " + self.post.post_title + " by poster " + self.post.user.username