import pytest
from pytest_lambda import lambda_fixture
from pytest_cases import fixture_ref, pytest_parametrize_plus

from . import models


def lazy_fixture_generator(mod):
    """
    Lazy = lazy_fixture_generator(globals())
    """
    ids = (x for x in range(1000))

    def Lazy(fun):
        """
        Lazy fixture loading from lambda

        Usage:
        @pytest_parametrize_plus("args", [Lazy(lambda f1, f2: (f1.atrr, f2.attr))])
        """
        name = f"lazy{next(ids)}"
        mod[name] = lambda_fixture(fun)
        return fixture_ref(name)
    return Lazy


Lazy = lazy_fixture_generator(globals())


@pytest.fixture
def book1():
    return models.Book(name="Moby Dick")


@pytest.fixture
def book2():
    return models.Book(name="Alice in Wonderland")


@pytest_parametrize_plus("name, expects", [
    (Lazy(lambda book1: book1.name), "Moby Dick"),
    (Lazy(lambda book2: book2.name), "Alice in Wonderland"),
])
@pytest.mark.django_db
def test_get_or_create_book(name, expects):
    book = models.Book.objects.get_or_create(name=name)[0]
    assert book.name == expects
