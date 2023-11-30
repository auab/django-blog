from django.db import models
from django.contrib.auth.models import User



STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Tag(models.Model):
    name=models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Categoria(models.Model):
    name=models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    introducao = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE, default=1)
    image = models.ImageField(upload_to='images', blank=True)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    tags = models.ManyToManyField(to=Tag, related_name="posts", blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
