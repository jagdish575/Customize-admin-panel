# Generated by Django 5.0.7 on 2024-07-18 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custmize', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
