from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils.text import slugify
from django.utils.translation import gettext as _
import os
import string
import random


# Create your models here.

def generate_random_string():
    str = "".join(random.choices(string.ascii_lowercase, k=10))
    return str


def convert_to_img(file_name):

    ppt_to_image_command = f'unoconv -f jpg certificate-data/{file_name}'
    os.system(ppt_to_image_command)

    img_file_name = os.path.splitext(str(file_name))[0]

    return f"{img_file_name}.jpg"


class UserManager(BaseUserManager):
    def create_user(self, email, name, tc, password=None, password2=None):
        if not email:
            raise ValueError("Admin must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            tc=tc
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, tc, password=None):
        user = self.create_user(
            email,
            password=password,
            name=name,
            tc=tc,
        )

        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="Email Address",
        max_length=255,
        unique=True
    )

    name = models.CharField(max_length=200)
    tc = models.BooleanField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'tc']

    def __str__(self):
        return str(self.id)

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=20, null=True, blank=True)
    subject = models.CharField(max_length=250, null=True, blank=True)
    event_department = models.CharField(max_length=20, null=True, blank=True)
    from_date = models.DateField()
    to_date = models.DateField()
    event_year = models.IntegerField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.event_name) + generate_random_string()
        return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)


class EventFile(models.Model):
    event_name = models.ForeignKey(Event, on_delete=models.CASCADE)
    xlsx_file = models.FileField(
        upload_to='certificates/csv_files/', null=True, blank=True)


class Participant(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    participant_name = models.CharField(max_length=50, null=True, blank=True)
    participant_id = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    phone = models.CharField(max_length=13, blank=True)
    certificate_status = models.CharField(max_length=10, null=True, blank=True)
    certificate_id = models.CharField(max_length=50, null=True, blank=True)
    certificate_sent_status = models.BooleanField(default=False)
    student_image = models.TextField(blank=True)


class CompletionCertificateTemplate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    template = models.FileField(
        upload_to='completion-certificate-templates/')
    template_img = models.ImageField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.template_img = convert_to_img(self.template.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)


class MeritCertificateTemplate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    template = models.FileField(
        upload_to='merit-certificate-templates/')
    template_img = models.ImageField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.template_img = convert_to_img(self.template)
        return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)


class ContributedCompletionCertificates(models.Model):
    template = models.FileField(
        upload_to='contributed-completion-certificate-templates/')
    template_img = models.ImageField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.template_img = convert_to_img(self.template)
        return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)


class ContributedMeritCertificates(models.Model):
    template = models.FileField(
        upload_to='contributed-merit-certificate-templates/')
    template_img = models.ImageField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.template_img = convert_to_img(self.template)
        return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)


class ParticipantAlbum(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, default=None)
    image_album = models.ImageField(
        upload_to='image-album/', null=True, blank=True)
