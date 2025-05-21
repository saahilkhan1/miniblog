from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title               = models.CharField(max_length=255,null=True,blank=True)
    content             = models.TextField(null=True,blank=True)
    author              = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    created_at          = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return f"{self.author} -- {self.title}"

class Like(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    post                = models.ForeignKey(Blog, on_delete=models.CASCADE,null=True,blank=True)
    like_post           = models.BooleanField(default=False,null=True,blank=True)
    created_at          = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f"{self.user.username} likes {self.post.title}"

class Comment(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    post                = models.ForeignKey(Blog, on_delete=models.CASCADE,null=True,blank=True)
    content             = models.TextField()
    created_at          = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}"
