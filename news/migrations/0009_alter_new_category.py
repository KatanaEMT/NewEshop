# Generated by Django 5.0 on 2024-07-23 12:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_alter_new_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.newscategory', verbose_name='Категория'),
        ),
    ]
