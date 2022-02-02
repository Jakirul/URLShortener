from django.db import models

# Create your models here.

class Main(models.Model):
    url = models.CharField(max_length=200)
    shortened_url = models.IntegerField(null=True, blank=True)



    def __str__(self):
        return f"{self.url} - {self.shortened_url}"