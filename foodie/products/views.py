# from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView

from .forms import FreeProductForm


# View for uploadng free products
class FreeProductUpload(LoginRequiredMixin, FormView):
    form_class = FreeProductForm
    template_name = "products/free_product_upload.html"
    success_url = "/products/free_product_upload/"

    def form_valid(self, form):
        return super().form_valid(form)
