from django.db import models
from django.urls import reverse


#Таблица каталога продуктов
class Item(models.Model):
    photo = models.ImageField(upload_to='products/')
    name = models.CharField(max_length=60, blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    desc = models.TextField(default="default description")
    category = models.CharField(max_length=30, choices=[('dessert', 'Десерт'), ('tea', 'Чай'), ('coffee', 'Кофе')], default="coffe")


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('item',
                       args=[self.name,
                             self.slug])
# #Таблица элементов корзины
# class Basket(models.Model):
#     photo = models.ForeignKey(Item, on_delete=models.CASCADE)
#     name = models.CharField(max_length=60, blank=False)
#     price = models.DecimalField(max_digits=5, decimal_places=2)
#     quantity = models.IntegerField()
#
# #Таблица заказов
# class Orders(models.Model):
#     order_id = models.IntegerField(primary_key=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     payment_method = models.CharField(max_length=60)
#     date_order = models.DateTimeField()