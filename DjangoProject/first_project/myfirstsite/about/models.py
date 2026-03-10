from django.db import models
from django.utils.text import slugify

class MenuItem(models.Model):
    """Простая модель позиции меню"""
    CATEGORY_CHOICES = [
        ('coffee', 'Кофе'),
        ('desserts', 'Десерты'),
        ('author', 'Авторские напитки'),
    ]
    
    category = models.CharField(
        'Категория', 
        max_length=20, 
        choices=CATEGORY_CHOICES,
        default='coffee'
    )
    name = models.CharField('Название', max_length=200)
    description = models.TextField('Описание', max_length=500)
    ingredients = models.CharField('Ингредиенты', max_length=300, blank=True)
    price = models.IntegerField('Цена')  # Используем IntegerField для простоты
    badge = models.CharField('Значок', max_length=50, blank=True, null=True)
    order = models.PositiveIntegerField('Порядок', default=0)
    is_active = models.BooleanField('Активно', default=True)
    
    class Meta:
        verbose_name = 'Позиция меню'
        verbose_name_plural = 'Позиции меню'
        ordering = ['category', 'order']
    
    def __str__(self):
        return f"{self.name} - {self.price}₽"


class MenuSettings(models.Model):
    """Настройки страницы меню"""
    delivery_text = models.CharField(
        'Текст доставки', 
        max_length=200,
        default='Действует доставка от 500₽'
    )
    footer_quote = models.CharField(
        'Цитата', 
        max_length=200,
        default='"Ваш любимый кофе ждет вас"'
    )
    page_title = models.CharField(
        'Заголовок страницы', 
        max_length=200,
        default='Меню - Уютная кофейня'
    )
    
    class Meta:
        verbose_name = 'Настройки меню'
        verbose_name_plural = 'Настройки меню'
    
    def __str__(self):
        return "Настройки страницы меню"
    
    def save(self, *args, **kwargs):
        if not self.pk and MenuSettings.objects.exists():
            # Не создаем новую запись, если уже есть
            return
        super().save(*args, **kwargs)