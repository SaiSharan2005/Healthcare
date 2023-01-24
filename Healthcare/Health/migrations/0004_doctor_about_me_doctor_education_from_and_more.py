# Generated by Django 4.1.1 on 2023-01-23 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Health', '0003_alter_doctor_street'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='About_me',
            field=models.TextField(default='Sai', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='Education_from',
            field=models.CharField(default='Sai', max_length=100),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='Profession',
            field=models.CharField(max_length=100),
        ),
    ]
