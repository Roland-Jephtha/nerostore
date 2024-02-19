from django.db import models
from django.contrib.auth.models import AbstractUser





class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length = 255, null = True)
    business_name = models.CharField(max_length = 255, null = True)

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"






class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    




class Profile(models.Model):
    
    business_name = models.CharField(max_length = 255, null = True)
    number = models.CharField(max_length = 255, null = True)
    email = models.EmailField(max_length=255, null = True)
    username = models.CharField(max_length=255, null = True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null = True)
    photo = models.ImageField(upload_to='profile', null = True, blank=True)
  
    
    def __str__(self):
        return str(self.business_name)

choice = (
        ("Phone", "Phone"),
        ("Laptop", "Laptop"),
        ("Accessories", "Accessories"),
        ("Games", "Games"),
        ("Clothing", "Clothing"),
        ("General", "General"),
        
    )




class Product(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null = True, )
    name = models.CharField(max_length=255)
    category = models.CharField(max_length = 255, choices=choice, null = True)

    quantity = models.IntegerField(null= True)
    description = models.TextField()
    price = models.DecimalField(max_digits=50, decimal_places=2)
    store = models.CharField(max_length=255, null = True)
    number = models.CharField(max_length=255, null = True)
    photo1 = models.ImageField(upload_to='products', null = True)
    photo2 = models.ImageField(upload_to='products', null= True, blank=True)
    photo3 = models.ImageField(upload_to='products', null= True, blank=True)
    photo4 = models.ImageField(upload_to='products', null= True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null  = True)

        
    def __str__(self):
        return self.name
    
    
    class Meta:
        ordering = ['-created']
    
    

class Payment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null = True, )
    account_name = models.CharField(max_length=255, blank = True)

    description = models.TextField(blank = True)
    Amount = models.DecimalField(max_digits=50, decimal_places=2)
    proof = models.ImageField(upload_to='payment', null = True)
    created = models.DateTimeField(auto_now_add=True, null  = True)

        
    def __str__(self):
        return self.account_name 
    
    
    class Meta:
        ordering = ['-created']
        
        
class PayRecord(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null = True, )
    account_name = models.CharField(max_length=255, blank = True)
    description = models.TextField(blank = True)
    amount = models.DecimalField(max_digits=50, decimal_places=2)
    proof = models.ImageField(upload_to='payment', null = True)
    created = models.DateTimeField(null  = True)

        
    def __str__(self):
        return str(self.account_name) + " " + "paid " + str(self.amount)
    
    
    class Meta:
        ordering = ['-created']
    
    
    







class Store(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null = True, related_name="store")
    name = models.CharField(max_length=255)
    paid = models.BooleanField(default=True, null = True)
            
    def __str__(self):
        return self.name
