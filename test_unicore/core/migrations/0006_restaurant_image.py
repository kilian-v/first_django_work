# Generated by Django 3.1.2 on 2020-10-02 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_restaurant_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(default='ook', upload_to=''),
            preserve_default=False,
        ),
    ]
