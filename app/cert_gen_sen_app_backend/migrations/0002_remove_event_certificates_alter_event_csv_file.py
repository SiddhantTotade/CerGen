# Generated by Django 4.1.3 on 2022-11-25 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cert_gen_sen_app_backend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='certificates',
        ),
        migrations.AlterField(
            model_name='event',
            name='csv_file',
            field=models.FileField(null=True, upload_to='certificates/csv_files/'),
        ),
    ]
