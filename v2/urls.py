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
from .views.v2 import (
  market_views as v2_market_views, 
  customer_views as v2_customer_views, 
  vendor_views as v2_vendor_views, 
  item_views as v2_item_views, 
  preorder_views as v2_preorder_views, #Not using this in v2
  weather_views as v2_weather_views, #Not using this in v2
  preorder2_vendors_views as v2_preorder2_vendors_views, 
  preorder2_customers_views as v2_preorder2_customers_views
)
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    # External APIs
    path('markets/location/<int:zipcode>/<int:radius>/', market_views.get_market_locations, name='get_market_locations'),
    path('weather/', weather_views.weather, name='weather'),
    
    # V2 Endpoints
    # markets
    path('api/v2/markets/', v2_market_views.market_list, name='market_list'),
    path('api/v2/markets/<int:market_id>/', v2_market_views.market_details, name='v2_market_details'),
    # vendors
    path('api/v2/markets/<int:market_id>/vendors/', v2_vendor_views.vendor_list, name='v2vendor_list'),
    path('api/v2/markets/<int:market_id>/vendors/<int:vendor_id>/', v2_vendor_views.vendor_details, name='v2_vendor_details'),
    # customers
    path('api/v2/markets/<int:market_id>/customers/', v2_customer_views.customer_list, name='v2_customer_list'),
    path('api/v2/markets/<int:market_id>/customers/<int:customer_id>/', v2_customer_views.customer_details, name='v2_customer_details'),
    # items
    path('api/v2/markets/<int:market_id>/vendors/<int:vendor_id>/items/', v2_item_views.item_list, name='v2_item_list'),
    path('api/v2/markets/<int:market_id>/vendors/<int:vendor_id>/items/<int:item_id>/', v2_item_views.item_details, name='v2_item_details'),
    # customer's preorders
    path('api/v2/markets/<int:market_id>/customers/<int:customer_id>/preorders2/', v2_preorder2_customers_views.preorder_customer_list, name='v2_preorder2_list'),
    path('api/v2/markets/<int:market_id>/customers/<int:customer_id>/preorders2/<int:preorder_id>/', v2_preorder2_customers_views.preorder_customer_details, name='v2_preorder2_details'),
    # vendor's preorders
    path('api/v2/markets/<int:market_id>/vendors/<int:vendor_id>/preorders2/', v2_preorder2_vendors_views.preorder_test_list, name='v2_preorder2_vendor_list'),
    path('api/v2/markets/<int:market_id>/vendors/<int:vendor_id>/preorders2/<int:preorder_id>/', v2_preorder2_vendors_views.preorder_test_details, name='v2_preorder2_vendor_details'),

    path('admin/', admin.site.urls),
]
