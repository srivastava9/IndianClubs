# Generated by Django 3.0.1 on 2020-04-28 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Club', '0004_auto_20200428_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='slug',
            field=models.SlugField(default='state_slug'),
        ),
    ]
