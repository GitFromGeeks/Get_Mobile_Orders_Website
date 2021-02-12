from django.contrib import admin
from .models import *

#SAMSUNG

@admin.register(banner_samsung)
class samsung_banner(admin.ModelAdmin):
    list_display=['banner']

@admin.register(Trending_samsung)
class Samsung_trending(admin.ModelAdmin):
 list_display = ('mobile_name','image','price')
 
#VIVO


@admin.register(banner_vivo)
class vivo_banner(admin.ModelAdmin):
    list_display=['banner']

@admin.register(Trending_vivo)
class vivo_trending(admin.ModelAdmin):
 list_display = ('mobile_name','image','price')
 


#OPPO


@admin.register(banner_oppo)
class oppo_banner(admin.ModelAdmin):
    list_display=['banner']

@admin.register(Trending_oppo)
class oppo_trending(admin.ModelAdmin):
 list_display = ('mobile_name','image','price')
 

#MI

@admin.register(banner_mi)
class mi_banner(admin.ModelAdmin):
    list_display=['banner']

@admin.register(Trending_mi)
class mi_trending(admin.ModelAdmin):
 list_display = ('mobile_name','image','price')
 


#REALME

@admin.register(banner_realme)
class realme_banner(admin.ModelAdmin):
    list_display=['banner']

@admin.register(Trending_realme)
class realme_trending(admin.ModelAdmin):
 list_display = ('mobile_name','image','price')
 
