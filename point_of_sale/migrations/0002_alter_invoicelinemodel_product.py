# Generated by Django 4.2.7 on 2024-02-18 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0006_reservemodel'),
        ('point_of_sale', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoicelinemodel',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.productmodel'),
        ),
    ]
