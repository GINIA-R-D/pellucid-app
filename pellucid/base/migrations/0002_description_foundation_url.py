# Generated by Django 4.0.6 on 2022-07-14 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='description',
            name='foundation_url',
            field=models.URLField(null=True),
        ),
    ]
