# Generated by Django 2.1.1 on 2018-09-30 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180930_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Gender'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='Phone'),
        ),
    ]