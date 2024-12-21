from django.contrib import admin
from django.urls import path
from eshop.products import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/products/',views.product_list_api_view)
]
