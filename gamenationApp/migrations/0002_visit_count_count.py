# Generated by Django 5.0.3 on 2024-03-25 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamenationApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit_count',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
