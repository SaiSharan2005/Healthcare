# Generated by Django 4.1.1 on 2023-01-23 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Health', '0004_doctor_about_me_doctor_education_from_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='About_me',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='Education_from',
            field=models.CharField(max_length=100),
        ),
    ]
