from django.shortcuts import render
from django.views.generic import TemplateView

from mainApp.models import Category, SubCategory, Products


class CatView(TemplateView):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'mainApp/index.html', context={'categories': categories})


class SubCatView(TemplateView):
    def get(self, request, name):
        subcategories = SubCategory.objects.filter(cat_name=name)
        products = Products.objects.filter(cat_name=name)
        return render(request, 'mainApp/subcat.html', context={'subcategories': subcategories,
                                                              'products': products})


class ProdView(TemplateView):
    def get(self, request, name):
        products = Products.objects.filter(sub_cat_name=name)
        return render(request, 'mainApp/prod.html', context={'products': products})


class CurProdView(TemplateView):
    def get(self, request, id):
        products = Products.objects.get(prod_id=id)
        return render(request, 'mainApp/curprod.html', context={'products': products})
