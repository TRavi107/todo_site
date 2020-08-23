from django.db import models
from django.contrib.auth import settings
from django.shortcuts import reverse 

# Create your models here.
class Todo_card(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,         
                            )

    title = models.CharField(max_length=20,default="MyList")
    slug = models.SlugField(blank=True,null=True)

    def get_detail_url(self):
        return reverse('core:card_detail',kwargs={
            'slug':self.slug
        })

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title
    
class Todo_Items(models.Model):
    content = models.CharField(max_length=1000)
    checked = models.BooleanField()
    card = models.ForeignKey(Todo_card,on_delete=models.CASCADE,blank=True,null=True)
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
