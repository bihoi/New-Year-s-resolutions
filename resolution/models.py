from django.db import models

class YourResolutions(models.Model):
    health = models.CharField(max_length=100)
    career = models.CharField(max_length=100)
    travel = models.CharField(max_length=100)

    def __str__(self):
        return self.health + ' - ' + self.career +' - '+ self.travel

class notes(models.Model):
    yourresolution = models.ForeignKey(YourResolutions, on_delete=models.CASCADE)
    note_title = models.CharField(max_length=1000)
