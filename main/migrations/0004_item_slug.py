# Generated by Django 5.0.4 on 2024-04-08 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_item_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]