from django.db import models
from django.urls import reverse


class Tool(models.Model):
    true = 'Not Available'
    false = 'Available'
    type_choices = [('POWER', 'power'), ('HAND', 'hand')]
    work_field_choices = [('WOODWORKING', 'woodworking'), ('GARDEN', 'garden'), ('MECHANICAL', 'mechanical')]
    name = models.CharField(max_length=250)
    type = models.CharField(max_length=250, choices=type_choices)
    work_field = models.CharField(max_length=250, choices=work_field_choices)
    manufacturer = models.CharField(max_length=250)
    replacement_cost = models.CharField(max_length=250)
    URL = models.TextField()
    condition = models.TextField()
    borrowed = models.BooleanField()
    owner = models.ForeignKey(
        'accounts.CustomUser',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')