# Generated by Django 5.0 on 2024-01-10 00:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market_nextdoor_api', '0007_rename_item_preorder_test_items'),
    ]

    operations = [
        migrations.RenameField(
            model_name='preorder_testitem',
            old_name='quantity',
            new_name='quantity_requested',
        ),
    ]
