# Generated by Django 5.1.6 on 2025-03-24 00:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_tracker', '0011_remove_usersgamesstat_completion'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersgamesstat',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game_tracker.game'),
        ),
        migrations.AddConstraint(
            model_name='usersgamesstat',
            constraint=models.UniqueConstraint(fields=('user', 'game'), name='unique_user_game_stat'),
        ),
    ]
