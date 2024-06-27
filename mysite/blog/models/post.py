from django.contrib.auth.models import User
from django.db import models

STATUS =  (
    (0, 'Draft'),
    (1, 'Publish')
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    # IDENTIFICAÇÃO DO POST
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        # FORMA DE ORDENAÇÃO
        ordering = ['-created_on']

        # SUBSCREVENDO O METODO ESPECIAL DO PYTHON PARA RETORNAR O NOME DOS POSTS
        def __str__(self):
            return self.title
