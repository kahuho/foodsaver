from allauth.utils import get_user_model
from django.contrib.gis.db import models

User = get_user_model()


# Create your models here.
class Products(models.Model):
    CATEGORY = [("f", "food"), ("nf", "non-food")]

    title = models.CharField(max_length=120)
    description = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    featured = models.BooleanField(default=False)
    category = models.CharField(max_length=20, choices=CATEGORY)
    quantity = models.IntegerField(default=1)
    image = models.ImageField(upload_to="products/", null=False, blank=False)
    pick_up_time = models.DateTimeField(null=True, blank=True)
    location = models.PointField(null=False)
    number_of_days_listed = models.IntegerField(default=14)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
