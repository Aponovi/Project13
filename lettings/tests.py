import pytest
from django.test import Client
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

from .models import Letting, Address


@pytest.mark.django_db(transaction=True, reset_sequences=True)
class Tests_Lettings_Views:

    def test_lettings_index_view(self):
        client = Client()
        expected_content_1 = "<h1>Lettings</h1>"
        expected_content_2 = "Wayne Manor"

        address = Address.objects.create(number=1007,
                                         street='Mountain Drive',
                                         city='Gotham City',
                                         state='NJ',
                                         zip_code='12345',
                                         country_iso_code='USA'
                                         )
        Letting.objects.create(title="Wayne Manor",
                               address_id=address.id)
        path = reverse('lettings:index')
        response = client.get(path)
        content = response.content.decode()

        assert expected_content_1 in content
        assert expected_content_2 in content
        assert response.status_code == 200
        assertTemplateUsed(response, "lettings/index.html")

    def test_lettings_letting_view(self):
        client = Client()
        expected_content_1 = "<h1>Wayne Manor</h1>"
        expected_content_2 = "<p>1007 Mountain Drive</p>"

        Address.objects.create(number=1007,
                               street='Mountain Drive',
                               city='Gotham City',
                               state='NJ',
                               zip_code='12345',
                               country_iso_code='USA'
                               )
        Letting.objects.create(title="Wayne Manor",
                               address_id=1)
        path = reverse('lettings:letting', kwargs={'letting_id': 1})
        response = client.get(path)
        content = response.content.decode()

        assert expected_content_1 in content
        assert expected_content_2 in content
        assert response.status_code == 200
        assertTemplateUsed(response, "lettings/letting.html")
