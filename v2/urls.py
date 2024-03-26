"""
URL configuration for market_nextdoor_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from .views import market_views, customer_views, vendor_views, item_views, customer_views, preorder_views, weather_views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    # External APIs
    path('markets/location/<int:zipcode>/<int:radius>/', market_views.get_market_locations, name='get_market_locations'),
    path('weather/', weather_views.weather, name='weather'),
    
    # V2 Endpoints
    # markets
    path('markets/', market_views.market_list, name='test_name'),
    path('markets/<int:market_id>/', market_views.market_details, name='test_name'),
    # vendors
    path('vendors/', vendor_views.vendor_list, name='test_name'),
    path('vendors/<int:vendor_id>/', vendor_views.vendor_details, name='test_name'),
    ## vendors by market
    path('markets/<int:market_id>/vendors/', vendor_views.vendors_by_market_list, name='test_name'),
    path('markets/<int:market_id>/vendors/<int:vendor_id>/', vendor_views.vendor_by_market_details, name='test_name'),
    # customers
    path('customers/', customer_views.customer_list, name='test_name'),
    path('customers/<int:customer_id>/', customer_views.customer_details, name='test_name'),
    ## customers by market
    path('markets/<int:market_id>/customers/', customer_views.customers_by_market_list, name='test_name'),
    path('markets/<int:market_id>/customers/<int:customer_id>/', customer_views.customer_by_market_details, name='test_name'),
    # items
    path('vendors/<int:vendor_id>/items/', item_views.item_list, name='test_name'),
    path('vendors/<int:vendor_id>/items/<int:item_id>/', item_views.item_details, name='test_name'),
    # customer's preorders
    path('markets/<int:market_id>/customers/<int:customer_id>/preorders/', customer_views.preorder_by_customer_list, name='test_name'),
    path('markets/<int:market_id>/customers/<int:customer_id>/preorders/<int:preorder_id>/', customer_views.preorder_by_customer_details, name='test_name'),
    # vendor's preorders
    path('markets/<int:market_id>/vendors/<int:vendor_id>/preorders/', vendor_views.preorder_by_vendor_list, name='test_name'),
    path('markets/<int:market_id>/vendors/<int:vendor_id>/preorders/<int:preorder_id>/', vendor_views.preorder_by_vendor_details, name='test_name')
]
