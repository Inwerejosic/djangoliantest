from django.db import models

# class college(Model): 
#     CollegeID = models.IntegerField(primary_key = True) 
#     name = models.CharField(max_length=50) 
#     strength = models.IntegerField() 
class drinks(models.Model):
    drink = models.CharField(max_length=200)
    price = models.IntegerField()    