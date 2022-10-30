from django.db import models

# Create your models here.
class Product(models.Model):

    name = models.CharField(max_length=100)
    sell_in = models.IntegerField()
    quality = models.IntegerField()

    class Meta:
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name

    #def get_absolute_url(self):
        #return reverse()