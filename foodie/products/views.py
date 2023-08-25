# Geodjango imports 
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance

# Django imports
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
#Internal imports 
from products.models import Products
from .forms import FreeProductForm, PaidProductForm, RequestProductorServiceForm



# View for form for uploadng free products
class FreeProductUpload(LoginRequiredMixin, CreateView):
    form_class = FreeProductForm
    template_name = "products/free_stuff_upload_form.html"
    success_url = "/free_product_form/"

#view for paid products upload 
class PaidProductUploadForm(LoginRequiredMixin, CreateView):
    form_class = PaidProductForm
    template_name = "products/paid_product_form.html"
    success_url = "/paid_product_form/"


#Service request form
class RequestProductorService(LoginRequiredMixin, CreateView):
    form_class = RequestProductorServiceForm
    template_name = "products/request_productor_service.html"
    success_url = "/request_product_or_service_form/"
    
    
        