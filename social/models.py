from distutils.command.upload import upload
from email.mime import audio, image
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count

# Create your models here.

class Posts(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    images=models.ImageField(upload_to="images",null=True,blank=True)
    created_date=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)

    @property                   
    def fetch_comments(self):
        comments=self.comments_set.all().annotate(up_count=Count('up_vote')).order_by('-up_count')
        return comments
        
    def __str__(self):
        return self.title

class Comments(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Posts,on_delete=models.CASCADE)
    comment=models.CharField(max_length=200)
    created_date=models.DateTimeField(auto_now_add=True)
    up_vote=models.ManyToManyField(User,related_name="upvotes") 

    def __str__(self):
        return self.comment

class User_detail(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=15,null=True,blank=True)
    images=models.ImageField(upload_to="images",null=True,blank=True)



