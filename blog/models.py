from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    pub_date = models.DateTimeField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
