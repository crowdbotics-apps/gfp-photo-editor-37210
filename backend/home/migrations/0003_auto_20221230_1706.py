# Generated by Django 2.2.26 on 2022-12-30 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_photos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photos',
            name='user',
        ),
        migrations.AddField(
            model_name='photos',
            name='photo_type',
            field=models.CharField(choices=[('original', 'original'), ('edit', 'edit'), ('collage', 'collage')], default='original', max_length=16),
        ),
    ]
