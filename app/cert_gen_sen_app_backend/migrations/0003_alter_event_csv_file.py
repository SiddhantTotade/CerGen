# Generated by Django 4.1.3 on 2022-11-25 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cert_gen_sen_app_backend', '0002_remove_event_certificates_alter_event_csv_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='csv_file',
            field=models.FileField(blank=True, null=True, upload_to='certificates/csv_files/'),
        ),
    ]
