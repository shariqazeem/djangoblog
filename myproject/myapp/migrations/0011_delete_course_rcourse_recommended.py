# Generated by Django 4.2.5 on 2023-10-19 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_imagemodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.AddField(
            model_name='rcourse',
            name='recommended',
            field=models.BooleanField(default=False),
        ),
    ]