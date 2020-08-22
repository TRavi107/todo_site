from django.db import models
from django.contrib.auth import settings
from django.shortcuts import reverse 

# Create your models here.
class Todo_Items(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                blank = True,
                                null=True          
                            )
    content = models.CharField(max_length=1000)
    checked = models.BooleanField()

    def __str__(self):
        return self.content

    def get_check_url(self):
        return reverse('core:action',kwargs={
            'id':self.id,
            'action':'check'
        })

    def get_edit_url(self):
        return reverse('core:action',kwargs={
            'id':self.id,
            'action':'edit'
        })

    def get_delete_url(self):
        return reverse('core:action',kwargs={
            'id':self.id,
            'action':'delete'
        })
