from django.db import models

class phone(models.Model):
 image1 = models.ImageField()
 image2 = models.ImageField()
 image3 = models.ImageField()
 image4 = models.ImageField()
 image5 = models.ImageField()
 company = models.CharField(max_length=50)
 mobile_name = models.CharField(max_length=300)
 color=models.CharField(max_length=20)
 price = models.CharField(max_length=20)
 RAM=models.CharField(max_length=10)
 storage=models.CharField(max_length=10)
 exp_storage=models.CharField(max_length=10)
 processor=models.CharField(max_length=50)
 front_camera=models.CharField(max_length=50)
 back_camera=models.CharField(max_length=50)
 dimension=models.CharField(max_length=50)
 weight=models.CharField(max_length=50)
 os=models.CharField(max_length=50)
 display_size=models.CharField(max_length=50)
 resolution=models.CharField(max_length=50)
 network_type=models.CharField(max_length=50)
 battery=models.CharField(max_length=50)
 warranty=models.CharField(max_length=50)

 def __str__(self):
     return self.mobile_name
