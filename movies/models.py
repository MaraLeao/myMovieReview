from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=150, blank=True, null=True)
    year = models.DateField(blank=True, null=True)
    plot = models.CharField(max_length=255)

    def __str__(self):
        return f'Title: {self.title}, Type: {self.type}, Year: {self.year}, Plot: {self.plot}'