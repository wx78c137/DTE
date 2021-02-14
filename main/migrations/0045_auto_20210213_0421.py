# Generated by Django 3.1.4 on 2021-02-13 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0044_auto_20210212_2123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='level',
            name='levelName',
        ),
        migrations.AddField(
            model_name='level',
            name='name',
            field=models.CharField(choices=[('gcse', 'THCS'), ('a-level-foundation', 'Dự bị đại học'), ('under-graduate', 'Đại học'), ('graduate', 'Thạc sĩ-Master'), ('research', 'Tiến sĩ-Nghiên cứu-Trợ lý giáo sư')], max_length=200, null=True),
        ),
    ]