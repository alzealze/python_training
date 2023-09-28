from fixture.application import Application
import pytest


@pytest.fixture(scope="session")
def app(request):
    """Создаем, разрушаем, возвращаем фикстуру"""
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
