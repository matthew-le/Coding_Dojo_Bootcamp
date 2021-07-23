from django.db import models


# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "Show title shoud be at least 2 characters"
        if len(postData['network']) < 3:
            errors['network'] = "Show Network should be at least 3 characters"
        if len(postData['desc']) < 10:
            errors['desc'] = "Show description should be at least 10 characters"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    desc = models.TextField(blank=True)
    objects = ShowManager()

    def __repr__(self):
        return f"<Show Information: {self.title} ({self.id})>"