# Generated by Django 5.0.6 on 2024-05-30 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='offer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='menu',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]