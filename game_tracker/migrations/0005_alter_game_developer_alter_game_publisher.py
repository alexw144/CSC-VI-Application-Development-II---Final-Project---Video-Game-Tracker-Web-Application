# Generated by Django 5.1.6 on 2025-03-15 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_tracker', '0004_remove_game_platform_game_other_game_pc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='developer',
            field=models.CharField(blank=True, max_length=35),
        ),
        migrations.AlterField(
            model_name='game',
            name='publisher',
            field=models.CharField(blank=True, max_length=35),
        ),
    ]
