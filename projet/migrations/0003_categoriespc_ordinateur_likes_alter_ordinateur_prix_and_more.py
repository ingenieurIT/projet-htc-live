# Generated by Django 4.0.1 on 2022-01-08 18:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projet', '0002_ordinateur_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriesPc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='ordinateur',
            name='likes',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='ordinateur',
            name='prix',
            field=models.FloatField(null=True),
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, null=True)),
                ('numero', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('photo_profil', models.ImageField(blank=True, null=True, upload_to='')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('utilisateur', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='ordinateur',
            name='categorie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='projet.categoriespc'),
        ),
    ]
