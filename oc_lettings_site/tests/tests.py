import pytest
from django.contrib.auth import get_user_model
from django.test import Client
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


def test_dummy():
    assert 1


@pytest.mark.django_db()
class Tests_Profiles_Views:

    def test_oc_lettings_site_index_view(self):
        client = Client()
        expected_content_1 = '<title>Holiday Homes</title>'
        expected_content_2 = '<h1>Welcome to Holiday Homes</h1>'
        path = reverse('index')
        response = client.get(path)
        content = response.content.decode()

        assert expected_content_1 in content
        assert expected_content_2 in content
        assert response.status_code == 200
        assertTemplateUsed(response, "index.html")
