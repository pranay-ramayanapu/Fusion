# Generated by Django 3.0.6 on 2020-05-22 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic_procedures', '0015_merge_20200522_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursesmtech',
            name='specialization',
            field=models.CharField(choices=[('Power and Control', 'Power and Control'), ('Microwave and Communication Engineering', 'Microwave and Communication Engineering'), ('Micro-nano Electronics', 'Micro-nano Electronics'), ('CAD/CAM', 'CAD/CAM'), ('Design', 'Design'), ('Manufacturing', 'Manufacturing'), ('CSE', 'CSE'), ('Mechatronics', 'Mechatronics'), ('MDes', 'MDes'), ('all', 'all')], max_length=40),
        ),
    ]