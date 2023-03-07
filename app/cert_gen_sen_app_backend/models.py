from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, User
from django.utils.text import slugify
from django.utils.translation import gettext as _

# Create your models here.


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

    def create_super_user(self, email, name, tc, password=None):
        user = self.create_user(
            email,
            password=password,
            name=name,
            tc=tc,
        )

        user.is_admin = True
        user.save(using=self._db)

        return user


# class User(AbstractBaseUser):
#     email = models.EmailField(
#         verbose_name="Email Address",
#         max_length=255,
#         unique=True
#     )

#     name = models.CharField(max_length=200)
#     tc = models.BooleanField()
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now_add=True)

#     object = UserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name', 'tc']

#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         return self.is_admin

#     def has_module_perm(self, app_label):
#         return True

#     @property
#     def is_staff(self):
#         return self.is_admin


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
        self.slug = slugify(self.event_name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)


class EventFile(models.Model):
    event_name = models.ForeignKey(Event, on_delete=models.CASCADE)
    xlsx_file = models.FileField(
        upload_to='certificates/csv_files/', null=True, blank=True)


class Participant(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=50, null=True, blank=True)
    student_id = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    certificate_status = models.CharField(max_length=10, null=True, blank=True)
    certificate_id = models.CharField(max_length=50, null=True, blank=True)
    certificate_sent_status = models.BooleanField(default=False)


# class CompletionCertificateTemplate(models.Model):
#     event = models.ForeignKey(Event, on_delete=models.CASCADE)
#     template = models.ImageField(upload_to='completion_certificates_templates')


# class MeritCertificateTemplate(models.Model):
#     event = models.ForeignKey(Event, on_delete=models.CASCADE)
#     template = models.ImageField(upload_to='merit_certificates_templates')


# class CompletionTemplateCoordinates(models.Model):
#     template = models.ForeignKey(Event, on_delete=models.CASCADE)
#     x_coor_name = models.IntegerField()
#     y_coor_name = models.IntegerField()
