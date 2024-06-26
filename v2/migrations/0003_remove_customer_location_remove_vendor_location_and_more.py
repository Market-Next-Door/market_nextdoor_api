# Generated by Django 5.0 on 2024-04-11 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v2', '0002_remove_preorder_items_preorder_item_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='location',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='location',
        ),
        migrations.AddField(
            model_name='customer',
            name='default_zipcode',
            field=models.CharField(default=80014, max_length=55),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customermarket',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default='2024-04-12 12:00:00'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customermarket',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='market',
            name='listing_id',
            field=models.CharField(default='default', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vendor',
            name='default_zipcode',
            field=models.CharField(default=80014, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vendormarket',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='vendormarket',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default='2024-04-12 12:00:00'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vendormarket',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='market',
            name='location',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
