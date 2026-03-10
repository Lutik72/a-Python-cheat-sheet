from .models import MenuItem, MenuSettings

def menu_context(request):
    """Добавляет данные меню в контекст всех шаблонов"""
    
    # Получаем все активные позиции меню
    menu_items = MenuItem.objects.filter(is_active=True).order_by('category', 'order')
    
    # Группируем по категориям
    menu_data = {
        'coffee': [],
        'desserts': [],
        'author': [],
    }
    
    for item in menu_items:
        menu_data[item.category].append(item)
    
    # Получаем настройки
    settings = MenuSettings.objects.first()
    
    return {
        'menu_items': menu_items,
        'coffee_items': menu_data['coffee'],
        'dessert_items': menu_data['desserts'],
        'author_items': menu_data['author'],
        'delivery_text': settings.delivery_text if settings else 'Действует доставка от 500₽',
        'footer_quote': settings.footer_quote if settings else '"Ваш любимый кофе ждет вас"',
    }