# Generated by Django 2.2.19 on 2021-04-12 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210412_0709'),
    ]

    operations = [
        migrations.AddField(
            model_name='bestoffers',
            name='discount_price',
            field=models.IntegerField(null=True),
        ),
    ]
