# Generated by Django 5.0 on 2024-01-06 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market_nextdoor_api', '0004_preorder_test_preorder_testitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preorder_test',
            name='quantity_requested',
        ),
    ]