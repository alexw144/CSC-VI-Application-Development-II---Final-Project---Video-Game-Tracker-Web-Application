# Generated by Django 5.1.6 on 2025-03-29 18:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_tracker', '0013_alter_review_game_review_unique_user_game_review'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=100)),
                ('post_body', models.TextField(blank=True)),
                ('post_image', models.ImageField(blank=True, null=True, upload_to='media/posts/')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('post_type', models.CharField(choices=[('Art', 'Art'), ('Img', 'Image'), ('Dis', 'Discussion'), ('Evt', 'Event'), ('Gui', 'Guide'), ('Annn', 'Announcement'), ('Hel', 'Help'), ('O', 'Other')], default='O', max_length=10)),
                ('game', models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='game_tracker.game')),
                ('user', models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
