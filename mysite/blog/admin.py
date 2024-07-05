from django.contrib import admin

# Register your models here.
from .models import Post


class PostAdmin(admin.ModelAdmin):
    # cRIA AS COLUNAS DA TABELA
    list_display = ("title", "slug", "status", "created_on")
    # CRIA UM FILTRO
    list_filter = ("status",)
    # CRIA UM CAMPO DE PESQUISA ONDE SERÁ POSSIVEL PESQUISAR PELO TITULO OU PELO CONTEUDO
    search_fields = ["title", "content"]
    # PREENCHE O CAMPO SLUG COM O TITLE
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
