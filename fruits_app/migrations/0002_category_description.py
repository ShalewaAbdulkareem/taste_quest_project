# Generated by Django 5.1.1 on 2024-10-11 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruits_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
