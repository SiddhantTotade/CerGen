# Generated by Django 4.1.3 on 2022-11-25 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cert_gen_sen_app_backend', '0003_alter_event_csv_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
