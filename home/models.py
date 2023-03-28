from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=300)
    subject = models.TextField(blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Feedback(models.Model):
    name = models.CharField(max_length=300)
    post = models.CharField(max_length=400)
    image = models.TextField()
    comment = models.TextField()

    def __str__(self):
        return self.name

STOCK = (('In stock', 'In stock'),('Out of stock','Out of stock'))
LABELS = (('Hot','Hot'),('New','New'),('Sale','Sale'),('','default'))
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    discounted_price = models.IntegerField(default = 0)
    image = models.ImageField(upload_to='media')
    description = models.TextField(blank=True)
    slug = models.TextField(unique=True)
    stock = models.CharField(max_length=100,choices=STOCK)
    label = models.CharField(max_length=100,choices=LABELS, blank=True)
    rank = models.IntegerField(null=True)


    def __str__(self):
        return self.name