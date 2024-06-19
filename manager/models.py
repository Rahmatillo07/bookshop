from django.contrib.auth.models import AbstractUser
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name







class User(AbstractUser):

    USER_ROLE_CHOICES = (
        ('admin','admin'),
        ('seller','seller'),
        ('user','user')
    )

    phone_number = models.CharField(max_length=13,blank=True,null=True)
    image = models.ImageField(upload_to='user/',null=True,blank=True,default='user/img.png')
    address = models.CharField(max_length=100,null=True,blank=True)
    user_role = models.CharField(max_length=10,choices=USER_ROLE_CHOICES,default='user')

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.username



class Book(models.Model):

    DISCOUNT_CHOICES = (
        ("Yo'q","Yo'q"),
        ('15%','15%'),
        ('5%','5%'),
        ('10%','10%'),
        ('50%','50%'),
    )

    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='book/')
    title = models.CharField(max_length=100)
    description = models.TextField(verbose_name='kitob haqida')
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    author = models.CharField(max_length=50,verbose_name='muallif')
    date_created = models.DateField(verbose_name='chiqarilgan vaqti')
    discount = models.CharField(max_length=10,choices=DISCOUNT_CHOICES,default="Yo'q")

    def __str__(self):
        return self.title + ' ' + self.author

    class Meta:
        unique_together = ['title']

    @property
    def total_price(self):
        return self.price * self.quantity


class Cart(models.Model):
    book = models.OneToOneField(Book,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.book.title





