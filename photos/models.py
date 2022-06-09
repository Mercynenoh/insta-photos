from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    pic = models.ImageField(upload_to = 'articles/',default='IMAGE')
    bio = models.TextField()
    # location = models.ForeignKey(Location, on_delete=models.CASCADE,default='LOCATION')
    
    # def save_image(self):
    #     self.save()

    # def save_bio(self):
    #     self.save()

    def __str__(self):
        return self.bio

class Post(models.Model):
    image = models.ImageField(upload_to = 'articles/',default='IMAGE')
    imagename =  models.CharField(max_length =30)
    caption = models.TextField()
    comments = models.TextField(default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    # location = models.ForeignKey(Location, on_delete=models.CASCADE,default='LOCATION')

    def __str__(self):
        return self.imagename

    def save_post(self):
        self.save()
