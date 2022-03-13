# Generated by Django 4.0.1 on 2022-01-13 01:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projet', '0008_alter_ordinateur_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='ordinateur',
            name='likes',
        ),
        migrations.AddField(
            model_name='message',
            name='likesM',
            field=models.ManyToManyField(blank=True, default=None, related_name='likesM', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ordinateur',
            name='likesO',
            field=models.ManyToManyField(blank=True, default=None, related_name='likesO', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='message',
            name='utilisateur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='utilisateur', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ordinateur',
            name='createur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='createur', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valeur', models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], default='like', max_length=10)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projet.ordinateur')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]