# Generated by Django 5.0 on 2023-12-27 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neobis_challenge', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total_price',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=10, null=True),
        ),
    ]
