# Generated by Django 5.0 on 2024-07-27 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costumerapp', '0004_costumer_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='profiles/', verbose_name='photo'),
        ),
    ]
