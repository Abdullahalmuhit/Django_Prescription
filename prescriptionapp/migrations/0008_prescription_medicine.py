# Generated by Django 2.2.3 on 2019-07-09 05:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('prescriptionapp', '0007_remove_prescription_medicine'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='medicine',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
