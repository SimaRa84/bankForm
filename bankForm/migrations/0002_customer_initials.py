# Generated by Django 5.0.6 on 2024-05-17 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankForm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='initials',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
