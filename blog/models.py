from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def comments(self):
        return Comments.objects.filter(answer_massage=self)

    class Meta:
        ordering = ['-date']


class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    massage = models.TextField()
    answer_massage = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True, related_name="pcomments")
    answer_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="rcomments")

    def __str__(self):
        return self.massage

    def ccomments(self):
        return Comments.objects.filter(answer_comment=self)

    class Meta:
        ordering = ['date']