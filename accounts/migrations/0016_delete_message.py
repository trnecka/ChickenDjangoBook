# Generated by Django 4.2.7 on 2024-01-13 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_alter_message_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
    ]