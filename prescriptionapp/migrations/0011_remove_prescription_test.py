# Generated by Django 2.2.3 on 2019-07-10 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prescriptionapp', '0010_auto_20190709_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prescription',
            name='test',
        ),
    ]