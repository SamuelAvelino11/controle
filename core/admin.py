from django.contrib import admin

from core.models import diaoperadores


# Register your models here.
class ProdAdmin(admin.ModelAdmin):
    list_display = ('id', 'operador', 'item', 'dia','quantidade','rejeicoes','aprovado')
    #list_filter = ('usuario', 'data_evento',)

admin.site.register(diaoperadores, ProdAdmin)