# Generated by Django 4.2.7 on 2023-12-18 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, default='default-avatar.png', null=True, upload_to='users'),
        ),
    ]
