from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.template.defaultfilters import slugify
from register.models import Accounts

CAR_TYPES = (
    ('Sedan','Sedan'),
    ('Limousine','Limousine'),
    ('Pickup','Pickup'),
    ('Hatchback','Hatchback'),
    ('Station Wagon','Station Wagon'),
    ('Liftback','Liftback'),
    ('Minivan','Minivan'),
    ('Coupe','Coupe'),
    ('Cabriolet','Cabriolet'),
    ('Roadster','Roadster'),
    ('Bodies out of classification','Bodies out of classification'),
)

GEARBOXES = (
    ("MANUAL","MANUAL"),
    ("ROBOTIC","ROBOTIC"),
    ("VARIABLE","VARIABLE"),
)

class Autos(models.Model):
    owner = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    brand = models.CharField(max_length=100)
    model_auto = models.CharField(max_length=50)
    transmisson = models.CharField(choices=GEARBOXES, max_length=100)
    type_of_body = models.CharField(choices=CAR_TYPES, max_length=100, null=True)
    produced_in = models.IntegerField(validators=[MinValueValidator(1899), MaxValueValidator(2023)])
    distance_km = models.IntegerField()

    def save(self,*args,**kwargs):
        self.slug=slugify(self.model_auto)
        return super().save(*args,**kwargs)

    def __str__(self):
        return self.model_auto