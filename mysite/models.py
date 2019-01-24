from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Me(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)#객체 생성시ㅏㄱ    #애네는 거의 필수로
    updated_at = models.DateTimeField(auto_now=True)#객체 변경시 간

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("mysite:Me_detail", kwargs={"Me_id": self.id})#디테일로가는데 포스트아이디가지고가자


class Ask(models.Model):
    nickname = models.CharField(max_length=100,default = "guest")
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)#객체 생성시ㅏㄱ    #애네는 거의 필수로
    updated_at = models.DateTimeField(auto_now=True)#객체 변경시 간

    def __str__(self):
        return self.text
    def get_absolute_url(self):
        return reverse("mysite:Ask_detail", kwargs={"Ask_id": self.id})#디테일로가는데 포스트아이디가지고가자

class Comment(models.Model):
    post = models.ForeignKey('mysite.Ask',on_delete=models.CASCADE,related_name='comments')
    nickname = models.CharField(max_length=200,default = "root")
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    #a=Post.objects.get(id=1)
    #a.comments=>글 a에 달린 comment들의 query set
    def __str__(self):
        return self.text
# Create your models here.
