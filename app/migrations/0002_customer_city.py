# Generated by Django 3.1.7 on 2021-03-01 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='city',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
