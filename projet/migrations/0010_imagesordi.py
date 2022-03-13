# Generated by Django 4.0.1 on 2022-01-17 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projet', '0009_remove_message_likes_remove_ordinateur_likes_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagesordi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photos', models.ImageField(blank=True, null=True, upload_to='')),
                ('ordinateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projet.ordinateur')),
            ],
        ),
    ]