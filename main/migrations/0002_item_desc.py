# Generated by Django 5.0.4 on 2024-04-08 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='desc',
            field=models.TextField(default='default description'),
        ),
    ]
