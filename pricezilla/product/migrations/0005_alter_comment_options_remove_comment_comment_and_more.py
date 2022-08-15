# Generated by Django 4.0.6 on 2022-08-14 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_image_product_url_alter_product_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on']},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='content',
            field=models.TextField(default=True, max_length=200),
        ),
        migrations.AddField(
            model_name='store',
            name='image',
            field=models.CharField(default='', max_length=255),
        ),
    ]