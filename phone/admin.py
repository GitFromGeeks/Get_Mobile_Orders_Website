from django.contrib import admin
from .models import *


@admin.register(phone)
class Samsung(admin.ModelAdmin):
 list_display = ('image1','image2','image3','image4','image5','company','mobile_name','color','price',
 'RAM','storage','exp_storage','processor','front_camera','back_camera','dimension','weight','os',
 'display_size','resolution','network_type','battery','warranty')