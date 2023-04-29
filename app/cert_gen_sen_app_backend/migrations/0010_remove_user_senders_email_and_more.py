# Generated by Django 4.1.3 on 2023-04-29 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cert_gen_sen_app_backend', '0009_user_senders_email_user_senders_password_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='senders_email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='senders_password',
        ),
        migrations.RemoveField(
            model_name='user',
            name='senders_phone',
        ),
        migrations.CreateModel(
            name='SendersCredentials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('senders_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('senders_password', models.CharField(blank=True, max_length=255, null=True)),
                ('senders_phone', models.CharField(blank=True, max_length=13, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]