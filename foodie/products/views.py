# Geodjango imports 
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance

# Django imports
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
#Internal imports 
from products.models import Products
from .forms import FreeProductForm


# View for uploadng free products
class FreeProductUpload(LoginRequiredMixin, FormView):
    form_class = FreeProductForm
    template_name = "products/free_stuff_upload_form.html"
    success_url = "/free_product_form/"

    def form_valid(self, form):
        latitude = form.cleaned_data['latitude']
        longtitude = form.cleaned_data['longtitude']
         # Create a Point object from latitude and longitude
        user_location = Point(longtitude, latitude, srid=4326) 
        # Example: Query your model to find nearest locations based on user input
        nearest_locations = Products.objects.annotate(distance=Distance('location', user_location)).order_by('distance')
        
        
        return super().form_valid(form)