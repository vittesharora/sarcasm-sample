# Generated by Django 2.0.13 on 2019-05-19 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='qimage',
            field=models.ImageField(blank=True, null=True, upload_to='game/static/'),
        ),
    ]
