# Generated by Django 3.1 on 2020-08-22 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_todo_items_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo_items',
            name='checked',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
