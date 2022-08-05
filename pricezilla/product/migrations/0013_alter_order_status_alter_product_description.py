# Generated by Django 4.0.6 on 2022-08-02 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_remove_order_tags_product_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Out of stock', 'Out of stock'), ('Available', 'Available'), ('Pending', 'Pending')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]