from django.contrib import admin
from .models import MenuItem, MenuSettings

# Регистрируем модель MenuItem и настраиваем админ‑панель
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    # Что показывать в списке позиций меню
    list_display = ('name', 'category', 'price', 'is_active')
    
    # По каким полям можно фильтровать список
    list_filter = ('category', 'is_active')
    
    # В каких полях искать при использовании поиска
    search_fields = ('name', 'description')


# Регистрируем модель MenuSettings и настраиваем админ‑панель
@admin.register(MenuSettings)
class MenuSettingsAdmin(admin.ModelAdmin):
    # Какие поля показывать в форме редактирования
    fields = ('page_title', 'delivery_text', 'footer_quote')
