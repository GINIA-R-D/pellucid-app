from django.db import models
from django.core.validators import MinLengthValidator
from django.core.validators import MaxLengthValidator

# Create your models here.

class Foundation(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Description(models.Model):
    name = models.CharField(max_length=200,null=True)
    foundation = models.ForeignKey(Foundation, on_delete=models.SET_NULL, null=True)
    short_description = models.TextField(null=True, blank=True,validators=[MaxLengthValidator(310, 'the field may only contain 310 characters.'),MinLengthValidator(150,'the field must have at least 150 characters.')])
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True,blank=True)
    foundations_url = models.TextField(blank=True, null=True)
    long_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name