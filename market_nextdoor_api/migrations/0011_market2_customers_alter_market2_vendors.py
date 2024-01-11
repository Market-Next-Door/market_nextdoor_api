# Generated by Django 5.0 on 2024-01-11 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market_nextdoor_api', '0010_customer2_vendor2_customer2market_market2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='market2',
            name='customers',
            field=models.ManyToManyField(through='market_nextdoor_api.Customer2Market', to='market_nextdoor_api.customer2'),
        ),
        migrations.AlterField(
            model_name='market2',
            name='vendors',
            field=models.ManyToManyField(through='market_nextdoor_api.Vendor2Market', to='market_nextdoor_api.vendor2'),
        ),
    ]
