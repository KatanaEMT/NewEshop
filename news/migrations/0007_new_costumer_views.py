# Generated by Django 5.0 on 2024-07-12 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costumerapp', '0003_profile'),
        ('news', '0006_new_views_qty'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='costumer_views',
            field=models.ManyToManyField(to='costumerapp.costumer'),
        ),
    ]
