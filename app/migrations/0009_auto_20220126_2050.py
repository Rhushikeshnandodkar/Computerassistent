# Generated by Django 3.2.9 on 2022-01-26 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='author',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='pages',
            field=models.IntegerField(null=True),
        ),
    ]