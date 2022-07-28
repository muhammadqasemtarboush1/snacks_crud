from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Snack


# Create your tests here.

class SnackTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='mark', email='mark@meta.com', password='markmeta'
        )
        self.snack = Snack.objects.create(
            title='lemon', description="So delicious", purchase=self.user
        )

    def test_list_status(self):
        url = reverse("snacks_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_template(self):
        url = reverse("snacks_list")
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')

    def test_str_method(self):
        self.assertEqual(str(self.snack), 'lemon')

    def test_detail_view(self):
        url = reverse('snack_detail', args=[self.snack.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'snack_detail.html')

    def test_create_view(self):
        url = reverse('create_snack')
        data = {
            "title": "shoco",
            "description": "what an amazing choice",
            "purchase": self.user.id
        }
        response = self.client.post(path=url, data=data, follow=True)
        self.assertTemplateUsed(response, 'snack_detail.html')
        self.assertRedirects(response, reverse('snack_detail', args=[2]))
        self.assertEqual(len(Snack.objects.all()), 2)

    def test_update_view(self):
        url = reverse('snack_update', args=[1])

        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_update.html')

    def test_delete_view(self):
        url = reverse("snack_delete", args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_base_correct_template(self):
        url = reverse('snacks_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, "base.html")
