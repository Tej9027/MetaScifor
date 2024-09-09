from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Movie(models.Model):
    # Fields for the movie table
    name = models.CharField(max_length=450)
    director = models.CharField(max_length=450)
    cast = models.CharField(max_length=1050)
    description = models.TextField(max_length=5500)
    release_date = models.DateField()
    averagerating = models.FloatField(default=0)
    image = models.URLField(default=None, null=True)

    def __str__(self):
        return self.name
    
    def __unicode__(self):
        return self.name
    

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1760)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.user.username