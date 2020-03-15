from django.urls import reverse
import pytest

@pytest.fixture
def response_login_view(client):
    return client.get(reverse("login"))

@pytest.fixture
def response_logout_view(client):
    return client.get(reverse("logout"))

@pytest.fixture
def response_menu_view(client):
    return client.get(reverse("menu"))

@pytest.fixture
def response_upload_view(client):
    return client.get(reverse("upload"))

@pytest.fixture
def response_download_view(client):
    return client.get(reverse("download"))