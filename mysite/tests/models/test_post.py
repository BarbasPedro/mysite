import pytest

from blog.factories import PostFactory

# CRIAMOS UMA FIXTURE
@pytest.fixture
def post_published():
    # CONSTRUIMOS O OBJETO PostFactory E DEMOS UM TITULO
    return PostFactory(title='pytest with factory')


@pytest.mark.django_db
# DECLARAMOS DENTRO DA FUNÇÃO O post_published
def test_create_published_post(post_published):
    # FIZEMOS UM assert PARA VERIFICAR SE O TITULO É O MESMO QUE DEFINIMOS
    assert post_published.title == 'pytest with factory'
