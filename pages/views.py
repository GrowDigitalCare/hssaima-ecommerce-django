from django.template.defaultfilters import capfirst, title
from superadmin import form
from superadmin.form import CategoryForm
from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from superadmin.models import *
from superadmin.serializers import *
from superadmin.form import *
from django.db.models import Q


class HomeView(View):

    def get(self, request, *args, **kwargs):
        template_name = 'website/home/home.html'
        category = CategoryModel.objects.all().order_by('-id')[:9]
        new_arrival = ProductModel.objects.all().order_by('-id')[:8]
        sale_product = ProductModel.objects.filter(~Q(sale_price=0))
        product_in_demand = ProductModel.objects.filter(product_in_demand = True)
        context = {
            'category': category,
            'new_arrival': new_arrival,
            'sale_product':sale_product,
            'product_in_demand': product_in_demand
        }
        return render(request, template_name,{'title':'Category','data':context})


class ShopView(View):

    def get(self, request, *args, **kwargs):
        template_name = 'website/shop/shop.html'
        category = CategoryModel.objects.all().order_by('-id')[:9]
        context = {
            'category': category
        }
        data = CategoryModel.objects.all()
        print(data)
        return render(request, template_name,{'title':'Category','data':context})

class checkoutView(View):

    def get(self, request, *args, **kwargs):
        template_name = 'website/checkout/checkout.html'
        category = CategoryModel.objects.all().order_by('-id')[:9]
        context = {
            'category': category
        }
        data = CategoryModel.objects.all()
        print(data)
        return render(request, template_name,{'title':'Category','data':context})

class Product_by_categoy(View):

    def get(self, request, slug, *args, **kwargs):
        template_name = 'website/shop/shop.html'
        cate = CategoryModel.objects.get(slug =slug)
        products = ProductModel.objects.filter(category_id = cate)
        print(products)
        context = {
            'products': products,
            # 'new_arrival': new_arrival
        }
        return render(request, template_name,{'title':'Category','data':context})



# class ContactView(View):

#     def get(self, request, *args, **kwargs):
#         template_name = 'website/Contact/contact_us.html'

#         return render(request, template_name)


class ContactView(View):
    # form_class = MyForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        template_name = 'website/Contact/contact_us.html'
        data = ContactModel.objects.all()
        # form = self.form_class(initial=self.initial)
        return render(request, template_name,{'title':'contact','data':data})

class PrivacyView(View):

    def get(self, request, *args, **kwargs):
        template_name = 'website/Privacy/privacy_policy.html'

        return render(request, template_name)

class RefundView(View):

    def get(self, request, *args, **kwargs):
        template_name = 'website/Refund/Refund_policy.html'

        return render(request, template_name)

class TermView(View):

    def get(self, request, *args, **kwargs):
        template_name = 'website/Terms/termsandconditions.html'

        return render(request, template_name)

class AboutView(View):

    def get(self, request, *args, **kwargs):
        template_name = 'website/about/about_us.html'

        return render(request, template_name)
