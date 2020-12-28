# Generated by Django 3.1.4 on 2020-12-23 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_level_subject_university'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='university',
        ),
        migrations.AddField(
            model_name='university',
            name='subjects',
            field=models.ManyToManyField(related_name='universities', to='main.Subject'),
        ),
    ]