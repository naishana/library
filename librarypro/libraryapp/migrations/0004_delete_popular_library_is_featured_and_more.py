# Generated by Django 5.1.3 on 2024-11-15 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0003_popular'),
    ]

    operations = [
        migrations.DeleteModel(
            name='popular',
        ),
        migrations.AddField(
            model_name='library',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='library',
            name='is_popular',
            field=models.BooleanField(default=False),
        ),
    ]
