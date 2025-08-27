from .models import Product
from django.views import View
from django.shortcuts import render
from django.http import JsonResponse

class PageHome(View):
    def get(self, request):
        return render(request, 'home.html')

class SearchProduct(View):
    def get(self, request):
        query = request.GET.get('q', '')
        
        search_products = Product.objects.filter(
           # title__icontains=query                   # __icontains - приблизителный поиск - тут не работает
            title__iregex=query                       # title__iregex - это работает - приблизителный поиск
        ).values('title', 'price', 'photo')                    # обычный словарь - список
        
        return JsonResponse({
            'success': True, 
            'query': query,
            'result': list(search_products),
            'count': len(search_products)             # кол-во продуктов которые успешно нашли
            }, status=200)
