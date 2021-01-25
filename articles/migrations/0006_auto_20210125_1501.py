# Generated by Django 2.2.13 on 2021-01-25 09:01

from django.db import migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20210125_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='categories',
            field=mptt.fields.TreeManyToManyField(blank=True, to='articles.Category'),
        ),
    ]
