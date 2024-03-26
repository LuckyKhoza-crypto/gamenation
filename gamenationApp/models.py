from django.db import models
from django.urls import reverse

from import_export import resources

# Create your models here.


class visit_count(models.Model):
    url = models.CharField(max_length=200, unique=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.url


class TrafficSource(models.Model):

    traffic_source = models.CharField(max_length=400, unique=True)
    views = models.IntegerField(default=0)
    watch_time = models.IntegerField(default=0)
    average_view_duration = models.TimeField(default='00:00:00')
    impressions = models.CharField(max_length=400, default=0)
    impressions_clicks = models.CharField(max_length=400, default=0)

    def __str__(self):
        return self.traffic_source


class TrafficSourceResource(resources.ModelResource):
    class Meta:
        model = TrafficSource
        import_fields = ['traffic_source', 'views', 'watch_time',
                         'average_view_duration', 'impressions', 'impressions_clicks']

        skip_unchanged = True

        use_bulk = True
