# Generated by Django 4.1.5 on 2023-04-17 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('New_Shop', '0015_promocode_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='promocode',
            old_name='code',
            new_name='promo_code',
        ),
    ]
