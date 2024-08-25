from django.db import models

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    userName = models.CharField(max_length=255, blank=True, null=True)
    userRating = models.IntegerField(blank=True, null=True)
    userReview = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Title: {self.title}, User name: {self.userName}, User rating: {self.userRating}, User review: {self.userReview}'