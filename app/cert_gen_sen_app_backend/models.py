from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class Event(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    event_name = models.CharField(max_length=20,null=True,blank=True)
    subject = models.CharField(max_length=20,null=True,blank=True)
    from_date = models.DateField()
    to_date = models.DateField()
    xlsx_file = models.FileField(upload_to='certificates/csv_files/',null=True,blank=True)
    slug = models.SlugField(null=True,blank=True)

    def save(self, *args,**kwargs):
        self.slug = slugify(self.event_name)
        return super().save(*args,**kwargs)

class Participant(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    email = models.EmailField(max_length=254,null=True,blank=True)