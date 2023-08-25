from django.urls import path

from .views import FreeProductUpload, PaidProductUploadForm, RequestProductorService

app_name = "products"
urlpatterns = [
    path("free_product_form/", FreeProductUpload.as_view(), name="free_product_form"),
    path("paid_product_form/", PaidProductUploadForm.as_view(), name="paid_product_form"),
    path("request_product_or_service_form/", RequestProductorService.as_view(), name="request_product_or_service_form"),


]
