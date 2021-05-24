# Generated by Django 2.2.19 on 2021-04-17 15:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0007_orders_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='ABL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BedSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('lowest_height', models.IntegerField()),
                ('highest_height', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Covered',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Display',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FilamentChamber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FilamentQuantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Height',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MotorDriver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Nozzle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UPSModule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WiFi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Profile_info',
            new_name='ProfileInfo',
        ),
        migrations.AddField(
            model_name='bestoffers',
            name='display',
            field=models.CharField(choices=[('touch', 'Touch'), ('knob', 'Knob'), ('touch+knob', 'Touch + Knob')], default='knob', max_length=100),
        ),
        migrations.AddField(
            model_name='bestoffers',
            name='filament',
            field=models.CharField(choices=[('1kg', '1kg'), ('2kg', '2kg'), ('3kg', '3kg')], default='1kg', max_length=100),
        ),
        migrations.AddField(
            model_name='bestoffers',
            name='nozzle',
            field=models.CharField(choices=[('single', 'Single'), ('double', 'Double')], default='single', max_length=100),
        ),
        migrations.AddField(
            model_name='orders',
            name='display',
            field=models.CharField(choices=[('touch', 'Touch'), ('knob', 'Knob'), ('touch+knob', 'Touch + Knob')], default='knob', max_length=100),
        ),
        migrations.AddField(
            model_name='orders',
            name='filament',
            field=models.CharField(choices=[('1kg', '1kg'), ('2kg', '2kg'), ('3kg', '3kg')], default='1kg', max_length=100),
        ),
        migrations.AddField(
            model_name='orders',
            name='nozzle',
            field=models.CharField(choices=[('single', 'Single'), ('double', 'Double')], default='single', max_length=100),
        ),
        migrations.AlterField(
            model_name='bestoffers',
            name='abl',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=100),
        ),
        migrations.AlterField(
            model_name='bestoffers',
            name='bed_size',
            field=models.CharField(choices=[('220x220', '220x220'), ('300x300', '300x300'), ('440x440', '440x440'), ('600x600', '600x600')], default='220x220', max_length=100),
        ),
        migrations.AlterField(
            model_name='bestoffers',
            name='cover',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=100),
        ),
        migrations.AlterField(
            model_name='bestoffers',
            name='filament_chamber',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=100),
        ),
        migrations.AlterField(
            model_name='bestoffers',
            name='height',
            field=models.CharField(choices=[('200', '200'), ('250', '250'), ('300', '300'), ('350', '350'), ('400', '400'), ('450', '450'), ('500', '500'), ('550', '550'), ('600', '600'), ('650', '650'), ('700', '700')], default='200', max_length=100),
        ),
        migrations.AlterField(
            model_name='bestoffers',
            name='motor_driver_type',
            field=models.CharField(choices=[('normal', 'Normal'), ('silent', 'Silent')], default='normal', max_length=100),
        ),
        migrations.AlterField(
            model_name='bestoffers',
            name='ups_module',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=100),
        ),
        migrations.AlterField(
            model_name='bestoffers',
            name='wifi',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=100),
        ),
        migrations.AlterField(
            model_name='orders',
            name='abl',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=100),
        ),
        migrations.AlterField(
            model_name='orders',
            name='bed_size',
            field=models.CharField(choices=[('220x220', '220x220'), ('300x300', '300x300'), ('440x440', '440x440'), ('600x600', '600x600')], default='220x220', max_length=100),
        ),
        migrations.AlterField(
            model_name='orders',
            name='cover',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=100),
        ),
        migrations.AlterField(
            model_name='orders',
            name='filament_chamber',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=100),
        ),
        migrations.AlterField(
            model_name='orders',
            name='height',
            field=models.CharField(choices=[('200', '200'), ('250', '250'), ('300', '300'), ('350', '350'), ('400', '400'), ('450', '450'), ('500', '500'), ('550', '550'), ('600', '600'), ('650', '650'), ('700', '700')], default='200', max_length=100),
        ),
        migrations.AlterField(
            model_name='orders',
            name='motor_driver_type',
            field=models.CharField(choices=[('normal', 'Normal'), ('silent', 'Silent')], default='normal', max_length=100),
        ),
        migrations.AlterField(
            model_name='orders',
            name='ups_module',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=100),
        ),
        migrations.AlterField(
            model_name='orders',
            name='wifi',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=100),
        ),
    ]