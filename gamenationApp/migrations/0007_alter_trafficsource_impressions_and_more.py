# Generated by Django 5.0.3 on 2024-03-25 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamenationApp', '0006_trafficsource_average_view_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trafficsource',
            name='impressions',
            field=models.CharField(default=0, max_length=400),
        ),
        migrations.AlterField(
            model_name='trafficsource',
            name='impressions_clicks',
            field=models.CharField(default=0, max_length=400),
        ),
    ]
