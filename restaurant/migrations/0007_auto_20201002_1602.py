# Generated by Django 3.1.2 on 2020-10-02 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0006_restaurant_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='city',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='state',
            new_name='number',
        ),
    ]
