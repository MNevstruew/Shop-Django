from django.contrib import admin
from unfold.admin import ModelAdmin
from appShop.models import *
from unfold.contrib.filters.admin import SliderNumericFilter        # Фигня типа слайдера справа
from unfold.contrib.filters.admin import AllValuesCheckboxFilter    # Фигня типа чекбоксов - коробочка с галочкой
from unfold.contrib.forms.widgets import WysiwygWidget              # Фигня добавляет виджет текстового редактора

@admin.register(Product)
class ProductAdmin(ModelAdmin):
    formfield_overrides = {               # Это значит что мы можем костамизировать          
        models.TextField:{                # Этот виджет работает только с текстовой историей - редактор текста
            'widget': WysiwygWidget,        
        }   
    }
    autocomplete_fields = ['category']    # Это встроено в django - открывает поиск для select
    list_display = ['title', 'category', 'price']
    list_display_links = ['title', 'category', 'price']
    search_fields = ['title', 'description']
    
    list_filter = [
        ('price', SliderNumericFilter),
        ('category__title', AllValuesCheckboxFilter)     
    ]
    list_filter_sheet = False            # сразу показывает слайдер
    list_filter_submit = True            # Включает кнопку чтоб слайдер работал

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ['title', 'position']
    list_display_links = ['title', 'position']
    search_fields = ['title']
    
    list_filter = [
        ('position', SliderNumericFilter)
    ]
    
    list_filter_sheet = False            # сразу показывает слайдер
    list_filter_submit = True            # Включает кнопку чтоб слайдер работал
    
    