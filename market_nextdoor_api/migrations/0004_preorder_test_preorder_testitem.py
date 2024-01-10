# Generated by Django 5.0 on 2024-01-06 23:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market_nextdoor_api', '0003_alter_item_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preorder_test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_requested', models.IntegerField(default=1)),
                ('ready', models.BooleanField(default=False)),
                ('packed', models.BooleanField(default=False)),
                ('fulfilled', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market_nextdoor_api.customer')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market_nextdoor_api.item')),
            ],
        ),
        migrations.CreateModel(
            name='Preorder_testItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market_nextdoor_api.item')),
                ('preorder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market_nextdoor_api.preorder_test')),
            ],
        ),
    ]
