# Generated by Django 5.1.6 on 2025-03-20 18:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_tracker', '0008_alter_game_slug'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='slug',
            field=models.SlugField(blank=True, max_length=200),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_title', models.CharField(max_length=100)),
                ('review_body', models.TextField()),
                ('game', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='game_tracker.game')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UsersGamesStat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_played', models.DurationField(default='00:00:00')),
                ('completion', models.BooleanField(null=True)),
                ('date_first_played', models.DateField(blank=True, null=True)),
                ('date_last_played', models.DateField(blank=True, null=True)),
                ('date_beaten', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('P', 'Playing'), ('PtP', 'Plan to Play'), ('C', 'Completed'), ('B', 'Beaten'), ('H', 'On Hold'), ('W', 'Wishlist'), ('R', 'Replaying'), ('O', 'Other')], default='O', max_length=10)),
                ('user_rating', models.CharField(blank=True, choices=[('-', 'Not Rated'), ('1', 'Appalling'), ('2', 'Horrible'), ('3', 'Very Bad'), ('4', 'Bad'), ('5', 'Average'), ('6', 'Fine'), ('7', 'Good'), ('8', 'Very Good'), ('9', 'Great'), ('10', 'Masterpiece')], default='O', max_length=10)),
                ('progress_percentage', models.FloatField(default=0.0)),
                ('achievement_count', models.ImageField(default=0, upload_to='')),
                ('notes', models.TextField(blank=True, null=True)),
                ('game', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='game_tracker.game')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_games_stats', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
