# Generated by Django 5.0 on 2024-07-12 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_new_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='views_qty',
            field=models.IntegerField(default=0),
        ),
    ]
