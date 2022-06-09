# Generated by Django 4.0.4 on 2022-06-09 19:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photos', '0005_followerscount_alter_profile_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='author',
            field=models.ForeignKey(default='',null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]