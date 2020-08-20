from django.db import models

# Create your models here.
class Customer(models.Model):
    class Meta:
        verbose_name = 'مشتری '
        verbose_name_plural = 'مشتری'
    CustomerName=models.CharField('نام',max_length=50)
    CustomerFamily=models.CharField('نام خانوادگی',max_length=50)
    CustomerAge=models.IntegerField('سن')
    Address = models.TextField('آدرس')

    def __str__(self):
        return F"{self.CustomerName} - {self.CustomerFamily} - {self.CustomerAge}"

class Product(models.Model):
    class Meta:
        verbose_name = 'کالا'
        verbose_name_plural = 'کالا'
    ProductName = models.CharField('نام کالا',max_length=50)
    ProductPrice=models.IntegerField('قیمت')
    Available=1
    NotAvailable=0
    status_choices=(
        (Available,'موجود در انبار'),
        (NotAvailable,'موجودی تا چند روز آینده'),
    )
    ProductStatus=models.IntegerField('وضعیت',choices=status_choices)


    def __str__(self):
        return F"{self.ProductName} - {self.ProductPrice}"

class OrderApp(models.Model):
    class Meta:
        verbose_name = 'سفارشات '
        verbose_name_plural = 'سفارشات'
    customer = models.ForeignKey('Customer',on_delete=models.PROTECT,verbose_name='مشتری')
    product = models.ForeignKey('Product',on_delete=models.PROTECT,verbose_name='کالا')
    OrderDate=models.DateTimeField('تاریخ ثبت سفارش')


    def __str__(self):
        return F"{self.customer} - {self.product} - {self.OrderDate}"