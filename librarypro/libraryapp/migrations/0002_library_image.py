# Generated by Django 5.1.3 on 2024-11-12 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='Image',
            field=models.ImageField(default=0, upload_to='images/'),
            preserve_default=False,
        ),
    ]
