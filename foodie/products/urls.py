from django.urls import path

from .views import FreeProductUpload

app_name = "products"
urlpatterns = [
    path("free_product_form/", FreeProductUpload.as_view(), name="free_product_form"),
]
