# Generated by Django 5.1.2 on 2024-10-30 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('python', '0002_contactus_userprogress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='Name',
            field=models.CharField(max_length=150),
        ),
    ]
