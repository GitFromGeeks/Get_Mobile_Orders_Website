from django.db import models

# SAMSUNG

class banner_samsung(models.Model):
    banner=models.ImageField()


class Trending_samsung(models.Model):
 image = models.ImageField()
 mobile_name = models.CharField(max_length=300)
 price = models.CharField(max_length=20)

 def __str__(self):
     return self.mobile_name


#VIVO

class banner_vivo(models.Model):
    banner=models.ImageField()


class Trending_vivo(models.Model):
 image = models.ImageField()
 mobile_name = models.CharField(max_length=300)
 price = models.CharField(max_length=20)

 def __str__(self):
     return self.mobile_name



#OPPO

class banner_oppo(models.Model):
    banner=models.ImageField()


class Trending_oppo(models.Model):
 image = models.ImageField()
 mobile_name = models.CharField(max_length=300)
 price = models.CharField(max_length=20)

 def __str__(self):
     return self.mobile_name


#MI


class banner_mi(models.Model):
    banner=models.ImageField()


class Trending_mi(models.Model):
 image = models.ImageField()
 mobile_name = models.CharField(max_length=300)
 price = models.CharField(max_length=20)

 def __str__(self):
     return self.mobile_name


#REALME

class banner_realme(models.Model):
    banner=models.ImageField()


class Trending_realme(models.Model):
 image = models.ImageField()
 mobile_name = models.CharField(max_length=300)
 price = models.CharField(max_length=20)

 def __str__(self):
     return self.mobile_name