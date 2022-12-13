from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class Event(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    event_name = models.CharField(max_length=20,null=True,blank=True)
    subject = models.CharField(max_length=20,null=True,blank=True)
    from_date = models.DateField()
    to_date = models.DateField()
    slug = models.SlugField(null=True,blank=True)

    def save(self, *args,**kwargs):
        self.slug = slugify(self.event_name)
        return super().save(*args,**kwargs)
    
    def __str__(self):
        return str(self.id)

class EventFile(models.Model):
    event_name = models.ForeignKey(Event,on_delete=models.CASCADE)
    xlsx_file = models.FileField(upload_to='certificates/csv_files/',null=True,blank=True)

class Participant(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    student_name = models.CharField(max_length=50,null=True,blank=True)
    email = models.EmailField(max_length=254,null=True,blank=True)
    certificate_status = models.CharField(max_length=10,null=True,blank=True)