# Generated by Django 4.1.1 on 2022-09-12 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='body',
            new_name='description',
        ),
        migrations.AddField(
            model_name='book',
            name='image_url',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
