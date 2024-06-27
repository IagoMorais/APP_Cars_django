from django.contrib import admin
from cars.models import Car, Brand#para inportar modulo e configuraaçoes
# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')#tabela que vai aparecer no meu site admin
    search_fields = ('model', 'brand', )#campo de busca buscar, onde quero que busque, parametros de busca 

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)
