from django.db import models

# Create your models here.


class visit_count(models.Model):
    url = models.CharField(max_length=200, unique=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.url
