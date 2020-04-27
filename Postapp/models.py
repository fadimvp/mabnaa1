from django.db import models

# Create your models here.
class PostList(models.Model):

    title=models.CharField(max_length=120)
    context = models.TextField()
    publish = models.DateTimeField(auto_now_add=True,auto_now=False)
    update = models.DateTimeField(auto_now_add=False,auto_now=True)

    def __str__(self):
        return self.title
class Home(models.Model):
    about1 =models.CharField(max_length=20) 
    body1 = models.TextField()
    title2 =models.CharField(max_length=20) 
    body2 = models.TextField(max_length=125)
    title3 =models.CharField(max_length=20) 
    body3 = models.TextField(max_length=125)
    def __str__(self):
        return self.about1