# Generated by Django 3.2.9 on 2022-01-26 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_rename_id_product_prodid'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
