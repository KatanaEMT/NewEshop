# Generated by Django 5.0 on 2024-07-12 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_new_costumer_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
