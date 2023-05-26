from django.db import models


class Statuses(models.Model):
    name = models.CharField(max_length=120)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'
