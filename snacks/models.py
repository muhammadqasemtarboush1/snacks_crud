from django.db import models
from django.contrib.auth import get_user_model

from django.urls import reverse

# Create your models here.

class Snack(models.Model):
    title = models.CharField(max_length=255, help_text="Snack title", default="Snack")
    purchase = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(default='Description', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Snack"
        verbose_name_plural = "Snacks"

    def get_absolute_url(self):
        return reverse('snack_detail', args=[self.id])
