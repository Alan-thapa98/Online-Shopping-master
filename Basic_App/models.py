from django.db import models


# Create your models here.

class home(models.Model):
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    price=models.FloatField()
    image=models.ImageField(upload_to='media/home')
    details=models.TextField()
    posted_on=models.DateTimeField(null=True,blank=True)


    def get_absolute_url(self):
        return reverse('Basic_App:product', kwargs={'pk': self.pk})
    def image_url(self):
        if self.image and hasattr(self.image,'url'):
            return self.image.url
    def __str__(self):
        return self.title
class Categori(models.Model):
    Category=models.CharField(max_length=200)


    def __str__(self):
        return self.Category


class Shop(models.Model):
    Category=models.CharField(max_length=200)
    title=models.ForeignKey('home',on_delete=models.CASCADE)
    price=models.FloatField()
    image=models.ImageField(upload_to='media/shop')
    details=models.TextField()
    posted_on=models.DateTimeField(null=True,blank=True)


    def get_absolute_url(self):
        return reverse('Basic_App:shopproduct', kwargs={'pk': self.pk})


    def image_url(self):
        if self.image and hasattr(self.image,'url'):
            return self.image.url
    def __str__(self):
        return self.Category
#class Product(models.Model):

class Checkout(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    c_name=models.CharField(max_length=100)
    email=models.EmailField()
    d=[("1","Bangladesh"),
       ("2","India"),
	   ("3","Mayanmar"),
	   ("4","Soudi Arabia"),
	   ("5","Pakistan"),
	   ("6","Canada"),
	   ("7","Malaysia"),
	   ("8","China"),
	   ("9","US"),
	   ("10","UK"),
       ('11','Other'),
       ]
    states=models.CharField(max_length=200,choices=d)
    address=models.CharField(max_length=200)
    town=models.CharField(max_length=200)
    zipcode=models.PositiveIntegerField()
    phone_number=models.IntegerField()
    comment=models.TextField()

    def __str__(self):
        return self.email
