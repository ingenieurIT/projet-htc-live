# Generated by Django 4.0.1 on 2022-02-03 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projet', '0012_admin'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ordinateur',
            options={'ordering': ['date_creation']},
        ),
        migrations.AddField(
            model_name='ordinateur',
            name='maj',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
