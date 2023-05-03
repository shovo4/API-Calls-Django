from django.db import models

# Create your models here.
class TVShow(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    network = models.CharField(max_length=50)
    episodes = models.IntegerField()
    cast = models.JSONField(default=list, blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    def __str__(self):
        return self.name

     