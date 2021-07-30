from django.contrib import admin
from Basic_App.models import home,Shop,Checkout,Categori

class homeadimin(admin.ModelAdmin):
    list_display=['__str__']
    search_fields=['__str__','title','prince']
    class Meta:
        model=home
admin.site.register(home,homeadimin)
class shopadimin(admin.ModelAdmin):
    list_display=['__str__','posted_on']
    search_fields=['__str__','price']
    list_per_page=10
    list_filter=['posted_on','Category']
    class Meta:
        model=Shop

admin.site.register(Shop,shopadimin)
class checkoutadimin(admin.ModelAdmin):
    list_display=['__str__','fname']
    search_fields=['__str__','email']
    list_per_page=10
    class Meta:
        model=Checkout

admin.site.register(Checkout,checkoutadimin)
admin.site.register(Categori)
