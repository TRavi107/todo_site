# Generated by Django 3.1 on 2020-08-22 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200822_0844'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo_card',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
