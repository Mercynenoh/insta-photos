from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    pic = models.ImageField(upload_to = 'articles/',default='IMAGE')
    bio = models.TextField(), 
    author = models.ForeignKey(User, on_delete=models.CASCADE, default="")

    
    def save_image(self):
        self.save()

    def save_bio(self):
        self.save()

class FollowersCount(models.Model):
    follower =  models.CharField(max_length =1000)
    user =  models.CharField(max_length =1000)

    def __str__(self):
        return self.user
    def save_user(self):
        self.save()


class Post(models.Model):
    image = models.ImageField(upload_to = 'articles/',default='IMAGE')
    imagename =  models.CharField(max_length =30)
    caption = models.TextField()
    comments = models.TextField(default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def save_post(self):
        self.save()

    def __str__(self):
        return self.imagename
    

    @classmethod
    def search_by_author(cls,search_term):
        pictures = cls.objects.filter(author__username__icontains=search_term)
        return pictures


   
