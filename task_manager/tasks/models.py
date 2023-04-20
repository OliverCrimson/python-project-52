from django.db import models
from task_manager.users import models as us
from task_manager.statuses import models as stat


# Create your models here.
class Tasks(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    made_by = models.ForeignKey(us.User, null=True)
    status = models.ForeignKey(stat.Statuses)
    executor = models.ForeignKey(us.User)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'
