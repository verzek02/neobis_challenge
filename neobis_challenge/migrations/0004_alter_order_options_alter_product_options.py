# Generated by Django 5.0 on 2023-12-21 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neobis_challenge', '0003_alter_category_options_alter_order_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
    ]