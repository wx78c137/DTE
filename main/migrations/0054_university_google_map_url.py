# Generated by Django 3.1.4 on 2021-02-18 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0053_remove_university_youtube_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='google_map_url',
            field=models.URLField(null=True),
        ),
    ]