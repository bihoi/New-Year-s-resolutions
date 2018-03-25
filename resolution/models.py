from django.db import models
from django.urls import reverse


class YourResolutions(models.Model):
    resolution_title = models.CharField(max_length=100)
    resolution_category = models.CharField(max_length=100)
    resolution_year = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('resolution:index')

    def __str__(self):
        return self.resolution_title + ' - ' + self.resolution_category +' - '+ self.resolution_year

class notes(models.Model):
    yourresolution = models.ForeignKey(YourResolutions, on_delete=models.CASCADE)
    note_title = models.CharField(max_length=500)
    note_content = models.CharField(max_length=5000)

    def __str__(self):
        return self.note_title
