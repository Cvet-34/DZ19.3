from django.contrib import admin
from .models import Buyer, Game


# Админ для модли Buyer
@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):  # admin.ModelAdmin позвляет регист. модели в админ
    list_display = ('name', 'balance', 'age')       # поле для отображения в списке
    list_filter = ('balance', 'age')                    #поле фильтрации
    search_fields = ('name',)      # поле для поиска
    list_per_page = 20              # колличество name на странице


readonly_fields = ('balance',)

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size')
    list_filter = ('size', 'cost')
    search_fields = ('title',)
    list_per_page = 20              # колличество игр на

# только для чтения поле balans



