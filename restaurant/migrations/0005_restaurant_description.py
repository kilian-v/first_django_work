# Generated by Django 3.1.2 on 2020-10-02 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_restaurant_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='description',
            field=models.TextField(default='the description'),
            preserve_default=False,
        ),
    ]
