# Generated by Django 5.0 on 2024-01-10 02:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market_nextdoor_api', '0008_rename_quantity_preorder_testitem_quantity_requested'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Preorder_testItem',
            new_name='Preorder2Item',
        ),
        migrations.CreateModel(
            name='Preorder2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ready', models.BooleanField(default=False)),
                ('packed', models.BooleanField(default=False)),
                ('fulfilled', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market_nextdoor_api.customer')),
                ('items', models.ManyToManyField(through='market_nextdoor_api.Preorder2Item', to='market_nextdoor_api.item')),
            ],
        ),
        migrations.AlterField(
            model_name='preorder2item',
            name='preorder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market_nextdoor_api.preorder2'),
        ),
        migrations.DeleteModel(
            name='Preorder_test',
        ),
    ]
