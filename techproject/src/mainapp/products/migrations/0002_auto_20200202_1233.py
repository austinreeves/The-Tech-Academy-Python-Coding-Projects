# Generated by Django 3.0.2 on 2020-02-02 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('treats', 'treats'), ('appetizers', 'appetizers'), ('entrees', 'entrees'), ('drinks', 'drinks')], max_length=60),
        ),
    ]
