# Generated by Django 2.2.19 on 2021-04-12 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bestoffers',
            name='belonging_order_id',
        ),
        migrations.RemoveField(
            model_name='bestoffers',
            name='outgoing',
        ),
    ]
