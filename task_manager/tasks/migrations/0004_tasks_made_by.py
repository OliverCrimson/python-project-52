# Generated by Django 4.1.7 on 2023-05-05 15:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0003_tasks_executor'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='made_by',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.PROTECT, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
    ]
