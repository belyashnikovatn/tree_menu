from django.db import models
from django.urls import reverse, NoReverseMatch


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    named_url = models.CharField(max_length=200, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    menu_name = models.CharField(max_length=100)

    def get_absolute_url(self):
        try:
            return reverse(self.named_url)
        except NoReverseMatch:
            return self.named_url

    def __str__(self):
        return self.name
