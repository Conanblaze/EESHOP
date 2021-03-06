# Generated by Django 4.0.2 on 2022-03-17 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('STORE', '0004_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('A', 'All')], default='All', max_length=10),
        ),
        migrations.AlterField(
            model_name='category',
            name='metal',
            field=models.CharField(choices=[('G', 'Gold'), ('S', 'Silver')], default='Silver', max_length=1),
        ),
    ]
