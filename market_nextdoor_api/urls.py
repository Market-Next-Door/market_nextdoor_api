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
from .views import market_views, customer_views, vendor_views, item_views, customer_views, preorder_views, weather_views, preorder2_vendors_views, preorder2_customers_views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('markets/', market_views.market_list, name='market_list'),
    path('markets/<int:market_id>/', market_views.market_details, name='market_details'),
    path('customers/', customer_views.customer_list, name='customer_list'),
    path('customers/<int:customer_id>/', customer_views.customer_details, name='customer_details'),
    path('vendors/', vendor_views.vendor_list, name='vendor_list'),
    path('vendors/<int:vendor_id>/', vendor_views.vendor_details, name='vendor_details'),
    path('vendors/<int:vendor_id>/items/', item_views.item_list, name='item_list'),
    path('vendors/<int:vendor_id>/items/<int:item_id>/', item_views.item_details, name='item_details'),
    path('customers/<int:customer_id>/preorders/', preorder_views.preorder_list, name='preorder_list'),
    path('customers/<int:customer_id>/preorders/<int:preorder_id>/', preorder_views.preorder_details, name='preorder_details'),
    path('vendors/<int:vendor_id>/preorders/', vendor_views.preorder_vendor_list, name='preorder_vendor_list'),
    path('vendors/<int:vendor_id>/preorders/<int:preorder_id>/', vendor_views.preorder_vendor_list_details, name='preorder_vendor_list_details'),
    path('markets/location/<int:zipcode>/<int:radius>/', market_views.get_market_locations, name='get_market_locations'),

    path('weather/', weather_views.weather, name='weather'),
    
    path('customers/<int:customer_id>/preorders2/', preorder2_customers_views.preorder_customer_list, name='preorder2_list'),
    path('customers/<int:customer_id>/preorders2/<int:preorder_id>/', preorder2_customers_views.preorder_customer_details, name='preorder2_details'),
    path('vendors/<int:vendor_id>/preorders2/', preorder2_vendors_views.preorder_test_list, name='preorder2_vendor_list'),
    path('vendors/<int:vendor_id>/preorders2/<int:preorder_id>/', preorder2_vendors_views.preorder_test_details, name='preorder2_vendor_details'),
    # Cascading endpoints
    # # vendors
    # path('markets/<int:market_id>/vendors/', views.vendor_list),
    # path('markets/<int:market_id>/vendors/<int:vendor_id>/', views.vendor_details),
    # # items
    # path('markets/<int:market_id>/vendors/<int:vendor_id>/items/', views.vendor_item_list),
    # path('markets/<int:market_id>/vendors/<int:vendor_id>/items/<int:item_id>/', views.vendor_item_details),
    # # customers
    # path('markets/<int:market_id>/customers/', views.customer_list),
    # path('markets/<int:market_id>/customers/<int:customer_id>/', views.customer_details),
    # # preorders
    # path('markets/<int:market_id>/customers/<int:customer_id>/preorders/', views.customer_preorder_list),
    # path('markets/<int:market_id>/customers/<int:customer_id>/preorders/<int:preorder_id>/', views.customer_preorder_details),
    path('admin/', admin.site.urls),
]
