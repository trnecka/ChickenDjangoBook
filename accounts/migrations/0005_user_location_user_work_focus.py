# Generated by Django 4.2.7 on 2023-12-19 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='work_focus',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
