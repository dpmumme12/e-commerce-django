# Generated by Django 3.1.1 on 2020-09-30 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_auto_20200927_2016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sales',
            old_name='buyer',
            new_name='buyer_id',
        ),
        migrations.RenameField(
            model_name='sales',
            old_name='seller_username',
            new_name='buyer_username',
        ),
        migrations.RenameField(
            model_name='sales',
            old_name='item',
            new_name='item_id',
        ),
        migrations.AddField(
            model_name='sales',
            name='seller_id',
            field=models.IntegerField(default=0),
        ),
    ]
