from django.forms.widgets import DateTimeBaseInput
from django.template.defaultfilters import capfirst, title
from rest_framework.fields import empty
from superadmin import form
from superadmin.form import CategoryForm
from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from superadmin.models import *
from superadmin.serializers import *
from superadmin.form import *
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.shortcuts import (get_object_or_404,
                              render, 
                              HttpResponseRedirect)
  
# Create your views here.
class MyDashboardView(View):
    # form_class = MyForm
    initial = {'key': 'value'}
    template_name = 'dashboard/dashboard.html'

    def get(self, request, *args, **kwargs):
        # form = self.form_class(initial=self.initial)
        return render(request, self.template_name,{"title":"Dashboard"})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name)


class CategoryView(View):
    # form_class = MyForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        template_name = 'dashboard/pages/category/view_category.html'
        data = CategoryModel.objects.all()
        print(data)
        # forms = CategoryForm()
        # form = self.form_class(initial=self.initial)
        return render(request, template_name,{'title':'Category','data':data})

    def post(self, request, *args, **kwargs):
        if form.is_valid():
            # <process form cleaned data>
            return redirect('category-form')

        return render(request, self.template_name)

class CategoryViewForm(View):
    # form_class = MyForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        template_name = 'dashboard/forms/category/category.html'
        form = CategoryForm()
        # form = self.form_class(initial=self.initial)
        return render(request, template_name,{'title':'Category','form':form})

    def post(self, request, *args, **kwargs):
        print(request.FILES)

        form = CategoryForm(request.POST,request.FILES)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('category-form')
        return redirect('/failed/')
        
# class CategoryDelete(View):
#     def get_object(self, slug):
#         try:
#             return CategoryModel.objects.get(slug=slug)
#         except CategoryModel.DoesNotExist:
#             return HttpResponseRedirect("/")
#     def delete(self, request, slug, format=None):
#         classes = self.get_object(slug)
#         classes.delete()
#         return redirect('category-form')
class CategoryDelete(View):
    initial = {'key': 'value'}
    def get(self,request, slug):
            data=CategoryModel.objects.filter(slug=slug)
            print(data)
            data.delete()
            return redirect('category-view')

def update_view(request, slug):
    context ={}
    obj = get_object_or_404(CategoryModel, slug = slug)
    form = CategoryForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('category-view')
    context["form"] = form
    return render(request, "dashboard/pages/category/update_category.html", context)

# def CategoryDelete(request, slug):
#     context ={}
#     obj = get_object_or_404(CategoryModel, slug = slug)
#     if request.method =="GET":
#         obj.delete()
#         return HttpResponseRedirect("/")
#     return render(request, "dashboard/pages/category/view_category.html", context)


# class CategoryEdit(UpdateView):
#     initial = {'key': 'value'}
#     model = CategoryModel
  
#     # specify the fields
#     fields = [
#         "title",
#         "image"
#     ]
  
    # can specify success url
    # url to redirect after successfully
    # updating details
    success_url ="/"


    # def get(self, request, slug):
    #     template_name = 'dashboard/forms/category/category.html'
    #     data = CategoryModel.objects.filter(slug=slug)
    #     form = CategoryForm()
    #     print(data)
    #     return render(request, template_name,{'title':'Category','data':data,'form':form})

    # def post(self, request, slug):
    #     data=CategoryModel.objects.filter(slug=slug)
    #     form = CategoryForm(self.request.POST or None, instance=data)
    #     print(form)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('category-form')
    #     return render(self,request, 'dashboard/pages/category/update_category.html', 
	# 	    {'form':form})
        
     		
# def update_event(request, event_id):
# 	event = Event.objects.get(pk=event_id)
# 	form = EventForm(request.POST or None, instance=event)
# 	if form.is_valid():
# 		form.save()
# 		return redirect('list-events')

# 	return render(request, 'events/update_event.html', 
# 		{'event': event,
# 		'form':form})
# class CategoryUpdate(UpdateView):
#     model = CategoryModel
#     fields = '__all__'
#     success_url = reverse_lazy('category-form')

# class CategoryDelete(DeleteView):
#     lookup_field = 'slug'
#     model = CategoryModel
#     fields = '__all__'
#     success_url = reverse_lazy('category-form')
# class CategoryUpdate(UpdateView):
#     model = CategoryModel
#     fields = ['title']

class ProductView(View):
    # form_class = MyForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        template_name = 'dashboard/pages/products/view_product.html'
        product = ProductModel.objects.all()
        context ={
            "item":product,
        }
        # form = self.form_class(initial=self.initial)
        return render(request, template_name,{'title':'Product','data':context})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return redirect('product-form')

        return render(request, self.template_name)


class ProductViewForm(View):
    # form_class = MyForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        template_name = 'dashboard/forms/product/product.html'
        # form = CategoryForm()
        category = CategoryModel.objects.all()
        item_fabric = FabricModel.objects.all()
        garments_care = GarmentModel.objects.all()
        print(garments_care)
        size = Size.objects.all()
        print(Sizes_choices)
        context = {
            'category':category,
            'item_fabric':item_fabric,
            'garments_care':garments_care,
            'number_of_days':NUMBER_OF_DAYS,
            'size':size,
        }
        print(size)
        # form = self.form_class(initial=self.initial)
        return render(request, template_name,{'title':'Product','context':context})

    def post(self, request, *args, **kwargs):
        template_name = 'dashboard/forms/product/product.html'
        print(request.POST)
        serializer = ProductSerializer(data={
            'title': request.POST['title'],
            'category': request.POST['category'],
            'short_description': request.POST['short_description'],
            'item_fabric': request.POST['item_fabric'],
            'sheila_included': request.POST['sheila_included'],
            'belt_included': request.POST['belt_included'],
            'garment_care': request.POST['garment_care'],
            'product_in_demand': request.POST['product_in_demand'],
            'color': request.POST['color'],
            'size': request.POST['size'],
            'quantity': request.POST['quantity'],
            'number_of_days': request.POST['number_of_days'],
            'tags': request.POST['tags'],
            'designer_note': request.POST['designer_note'],
            'total': request.POST['total'],
        })
        print(request.FILES.getlist('image'))

        if serializer.is_valid():
            product_id = serializer.save()
            images = request.FILES.getlist('image')
            # sales = request.data.get('sale_price')

            if images:
                for img in images:
                    ProductImgModel.objects.create(product_id=product_id ,image=img)
            return redirect('product-form')
        return HttpResponseRedirect('/failed/')


class ProductSaleView(View):
    
    def get(self, request, format=None):
        template_name = 'dashboard/pages/sale/sale.html'
        data = ProductModel.objects.filter(~Q(sale_price=0))
        context ={
            'item':data
        }
        
        return render(request, template_name,{'title':'Sale Product','data':context})

class ProductDeleteView(View):
    
    def get(self,slug, request, format=None):
        print(slug)
        template_name = 'dashboard/forms/sale/sale.html'
        data = ProductModel.objects.filter(sale_price=True)
        print(data)
        
        return render(request, template_name,{'data':data})


class FabricView(View):
    # form_class = MyForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        template_name = 'dashboard/pages/fabric/view_fabric.html'
        data = FabricModel.objects.all()
        # form = self.form_class(initial=self.initial)
        return render(request, template_name,{'title':'Fabric','data':data})
class FabricViewForm(View):
    # form_class = MyForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        template_name = 'dashboard/forms/fabric/fabric.html'
        form = FabricForm()

        # form = self.form_class(initial=self.initial)
        return render(request, template_name,{'title':'Fabric','form':form})

    def post(self, request, *args, **kwargs):
        template_name = 'dashboard/forms/fabric/fabric.html'
        form = FabricForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('fabric-form')
        return render(request, template_name,{'title':'Fabric'})

class FabricDelete(View):
    initial = {'key': 'value'}
    def get(self,request, slug):
            data=FabricModel.objects.filter(slug=slug)
            print(data)
            data.delete()
            return redirect('fabric-view')


def update_fabric(request, slug):
    context ={}
    obj = get_object_or_404(FabricModel, slug = slug)
    form = FabricForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('fabric-view')
    context["form"] = form
    return render(request, "dashboard/pages/fabric/update_fabric.html", context)


class GarmentView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'dashboard/pages/garment/view_garment.html'
        data = GarmentModel.objects.all()
        print(data)
        # form = self.form_class(initial=self.initial)
        return render(request, template_name,{'title':'Garment','data':data})
class GarmentViewForm(View):
    # form_class = MyForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        template_name = 'dashboard/forms/garment/garment.html'
        form = GarmentForm()

        # form = self.form_class(initial=self.initial)
        return render(request, template_name,{'title':'Garment','form':form})

    def post(self, request, *args, **kwargs):
        template_name = 'dashboard/forms/garment/garment.html'
        form = GarmentForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('garment-form')
        return render(request, template_name,{'title':'Garment'})

class GarmentDelete(View):
    initial = {'key': 'value'}
    def get(self,request, slug):
            data=GarmentModel.objects.filter(slug=slug)
            print(data)
            data.delete()
            return redirect('garment-view')


def update_garment(request, slug):
    context ={}
    obj = get_object_or_404(GarmentModel, slug = slug)
    form = GarmentForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('garment-view')
    context["form"] = form
    return render(request, "dashboard/pages/garment/update_garment.html", context)


class OrderView(View):
    # form_class = MyForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        template_name = 'dashboard/pages/order/view_order.html'

        # form = self.form_class(initial=self.initial)
        return render(request, template_name)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return redirect('order-form')

        return render(request, self.template_name)



class ProductDemandView(View):
    # form_class = MyForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        template_name = 'dashboard/pages/product/view_demandProduct.html'
        data = ProductDemandModel.objects.all()
        print(data)
        # form = self.form_class(initial=self.initial)
        return render(request, template_name,{'title':'Product','data':data})

class ProductDemandForm(View):
    # form_class = MyForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        template_name = 'dashboard/forms/Demand/demandProduct.html'
        form = ProductDemandForm()

        # form = self.form_class(initial=self.initial)
        return render(request, template_name,{'title':'Fabric','form':form})

    def post(self, request, *args, **kwargs):
        template_name = 'dashboard/forms/Demand/demandProduct.html'
        form = ProductDemandForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')
        return render(request, template_name,{'title':'Fabric'})

class RandomCouponView(View):
    queryset = RandomCoupon.objects.all().order_by('id')

class CouponView(View):
    queryset = Coupon.objects.all().order_by('id')



class sizeView(View):
    # form_class = MyForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        template_name = 'dashboard/pages/size/view_size.html'
        data = Size.objects.all()
        print(data)
        # form = self.form_class(initial=self.initial)
        return render(request, template_name,{'sizes':'size','data':data})

class sizeViewForm(View):
    # form_class = MyForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        template_name = 'dashboard/forms/size/size.html'
        form = sizeForm()

        # form = self.form_class(initial=self.initial)
        return render(request, template_name,{'sizes':'size','form':form})

    def post(self, request, *args, **kwargs):
        template_name = 'dashboard/forms/size/size.html'
        form = sizeForm(request.POST)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')
        return render(request, template_name,{'sizes':'size'})

class SaleView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'dashboard/forms/sale/sale.html'
        product = ProductModel.objects.all()
        context = {
            'product' : product
        }
        return render(request, template_name,{'data':context})

    def post(self,request,*args, **kwargs):

        products = request.POST.getlist('products')
        product_price_percentage = request.POST.get('percentage')
        print(request.POST)
        for product in products:
            item = ProductModel.objects.get(slug=product)
            item.get_sale_price(int(product_price_percentage))
        return redirect('sale-form')

class SaleDeleteView(View):
    def post(self, request,slug, *args, **kwargs):
        template_name = 'dashboard/pages/sale/sale.html'
        product = ProductModel.objects.all()
        context = {
            'product' : product
        }
        return render(request, template_name,{'title':'Sale View','data':context})

class SaleEditView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'dashboard/pages/sale/sale.html'
        product = ProductModel.objects.all()
        context = {
            'product' : product
        }
        return render(request, template_name,{'title':'Sale View','data':context})


class SaleFormView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'dashboard/forms/sale/sale.html'
        product = ProductModel.objects.all().order_by('-id')
        context = {
            'product' : product
        }
        return render(request, template_name,{'sizes':'size','data':context})

    def post(self, request, *args, **kwargs):
        template_name = 'dashboard/forms/sale/sale.html'
        form = sizeForm(request.POST)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')
        return render(request, template_name,{'sizes':'size'})


class BlogView(View):
    # form_class = MyForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        template_name = 'dashboard/pages/blog/view_blog.html'
        data = BlogModel.objects.all()
        print(data)
        # forms = blogForm()
        # form = self.form_class(initial=self.initial)
        return render(request, template_name,{'title':'blog','data':data})

    def post(self, request, *args, **kwargs):
        if form.is_valid():
            # <process form cleaned data>
            return redirect('blog-form')
        return render(request, self.template_name)

class BlogViewForm(View):
    # form_class = MyForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        template_name = 'dashboard/forms/blog/blog.html'
        form = BlogForm()
        # form = self.form_class(initial=self.initial)
        return render(request, template_name,{'title':'blog','form':form})

    def post(self, request, *args, **kwargs):
        form = BlogForm(request.POST)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('blog-form')
        return redirect('/failed/')
        
class BlogDelete(View):
    initial = {'key': 'value'}
    def get(self,request, slug):
            data=BlogModel.objects.filter(slug=slug)
            print(data)
            data.delete()
            return redirect('blog-view')


def update_blog(request, slug):
    context ={}
    obj = get_object_or_404(BlogModel, slug = slug)
    form = BlogForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('blog-view')
    context["form"] = form
    return render(request, "dashboard/pages/blog/update_blog.html", context)


class SliderView(View):
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        template_name = 'dashboard/pages/slider/view_slider.html'
        data = SliderModel.objects.all()
        print(data)
        return render(request, template_name,{'title':'Slider','data':data})

    def post(self, request, *args, **kwargs):
        if form.is_valid():
            return redirect('slider-form')
        return render(request, self.template_name)

class SliderViewForm(View):
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        template_name = 'dashboard/forms/slider/slider.html'
        form = SliderForm()
        print(form)
        return render(request, template_name,{'title':'Slider','form':form})

    def post(self, request, *args, **kwargs):
        print(request.FILES)
        form = SliderForm(request.POST,request.FILES)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('slider-form')
        return redirect('/failed/')
        

class SliderDelete(View):
    initial = {'key': 'value'}
    def get(self,request, slug):
            data=SliderModel.objects.filter(slug=slug)
            print(data)
            data.delete()
            return redirect('slider-view')


def update_slider(request, slug):
    context ={}
    obj = get_object_or_404(SliderModel, slug = slug)
    form = SliderForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('slider-view')
    context["form"] = form
    return render(request, "dashboard/pages/slider/update_slider.html", context)

