# Generated by Django 3.2.3 on 2021-05-21 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_avodha_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='img',
            field=models.ImageField(default='degault.jpg', upload_to='images'),
            preserve_default=False,
        ),
    ]
