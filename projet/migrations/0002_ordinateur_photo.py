# Generated by Django 4.0.1 on 2022-01-08 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordinateur',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
