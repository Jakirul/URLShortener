from django.db import models

# Create your models here.

class Main(models.Model):
    url = models.CharField(max_length=200)
    shortened_url = models.IntegerField(null=True, blank=True)



    def _str_(self):
        return self.url + self.shortened_url