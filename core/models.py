from django.db import models
from django.contrib.auth import settings

# Create your models here.
class Todo_Items(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                blank = True,
                                null=True          
                            )
    content = models.CharField(max_length=1000)
