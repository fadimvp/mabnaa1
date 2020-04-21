from django.contrib import admin
from Postapp.models import PostList
# Register your models here.




class AdminPost(admin.ModelAdmin):
    list_display = ['title','context','update','publish']
    class Meta :
        model = PostList
admin.site.register(PostList,AdminPost)