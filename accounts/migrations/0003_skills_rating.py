# Generated by Django 4.2.7 on 2024-01-07 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_skills_level_alter_skills_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='skills',
            name='rating',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, '★☆☆'), (2, '★★☆'), (3, '★★★')], null=True),
        ),
    ]