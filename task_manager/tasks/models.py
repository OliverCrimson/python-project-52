from django.db import models
from users.models import User
from statuses.models import Statuses
from labels.models import Labels



class Tasks(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField()
    status = models.ForeignKey(Statuses, on_delete=models.PROTECT)
    executor = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
    # label = models.ForeignKey(Labels, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name}'
