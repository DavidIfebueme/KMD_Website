from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(blank=True)
    amazon_link = models.URLField()