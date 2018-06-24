from django.db import models
from django.utils import timezone

class Drop(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    drop_description = models.TextField()
    drop_image = models.ImageField()

    def __str__(self):
        return self.name
