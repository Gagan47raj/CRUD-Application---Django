from django.db import models

class CustomerModel(models.Model):
    customername = models.CharField(max_length=100)
    customerphone = models.CharField(max_length=100)
    customeraddress = models.CharField(max_length=200)
    customeremail = models.CharField(max_length=50)
    customerpassword = models.CharField(max_length=20)

    class Meta:
        db_table = "customer"