from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  path('admin/', admin.site.urls),
  path('api/v1/', include('v1.urls')),
  path('api/v2/', include('v2.urls'))
  # path(include('v2.urls'))
]
