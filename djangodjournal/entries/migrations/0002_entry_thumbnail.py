# Generated by Django 2.1 on 2018-09-27 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
