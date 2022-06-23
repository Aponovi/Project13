import pytest
from django.test import Client
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

from .models import Letting, Address


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_letting_index_view():
    client = Client()
    Address.objects.create(number=1007,
                           street='Mountain Drive',
                           city='Gotham City',
                           state='NJ',
                           zip_code='12345',
                           country_iso_code='USA'
                           )
    Letting.objects.create(title="Wayne Manor",
                           address_id=1)
    path = reverse('lettings:index')
    response = client.get(path)
    content = response.content.decode()
    expected_content = "<h1>Lettings</h1>"

    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/index.html")
