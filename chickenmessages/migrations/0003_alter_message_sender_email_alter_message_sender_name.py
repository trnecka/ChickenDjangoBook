# Generated by Django 4.2.7 on 2024-01-13 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chickenmessages', '0002_alter_message_sender_email_alter_message_sender_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='sender_email',
            field=models.EmailField(default='Your mail', max_length=254),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender_name',
            field=models.CharField(default='Your name', max_length=100),
        ),
    ]
