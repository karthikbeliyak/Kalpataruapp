from django.db import models
    
class Plant(models.Model):
    category = models.CharField(max_length= 100)
    name= models.CharField(max_length= 100, db_index= True)
    #slug = models.SlugField(max_length=150, unique=True, db_index=True)
    description = models.TextField(max_length= 300, db_index=True)
    price= models.DecimalField(max_digits=10, decimal_places= 2)
    image = models.ImageField(upload_to='media/', blank=True)
   
    def __str__(self):
        return self.name