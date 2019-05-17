from django.db import models

class Job(models.Model):
    image = models.ImageField(default='image.jpeg', upload_to='images/')
    # image_url = models.CharField(default="https://s3.eu-west-2.amazonaws.com/django-static-files-1234/images/", max_length=400)
    summary = models.CharField(max_length=200)
    github_url = models.CharField(default="https://github.com/SzymonLudyga/", max_length=200)
