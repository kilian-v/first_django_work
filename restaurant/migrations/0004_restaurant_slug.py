# Generated by Django 3.1.2 on 2020-10-02 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_restaurant'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='slug',
            field=models.SlugField(default='test-restaurant'),
            preserve_default=False,
        ),
    ]
