# Generated by Django 3.2 on 2024-05-17 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jumia', '0005_alter_smartphone_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartphone',
            name='brand',
            field=models.CharField(max_length=255),
        ),
    ]
