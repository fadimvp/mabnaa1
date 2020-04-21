from django.db import models

# Create your models here.
class PostList(models.Model):

    title=models.CharField(max_length=120)
    context = models.TextField()
    publish = models.DateTimeField(auto_now_add=True,auto_now=False)
    update = models.DateTimeField(auto_now_add=False,auto_now=True)

    def __str__(self):
        return self.title