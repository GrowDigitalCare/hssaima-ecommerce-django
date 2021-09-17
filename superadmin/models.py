from django.db import models
from django.db.models.fields import CharField
from django.template.defaultfilters import slugify
import random
from django.urls import reverse

# Create your models here.
class CategoryModel(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    image = models.ImageField(upload_to ="static/category/")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('category_edit', kwargs={'pk': self.pk})

    def get_product_by_category(self):
        return reverse('product_by_category', kwargs={
            'slug': self.slug,
            }
        )
    def get_absolute_url_edit(self):
        return reverse('category-edit', kwargs={'slug': self.slug})

    def get_absolute_url_delete(self):
        return reverse('category-delete', kwargs={'slug': self.slug})





NUMBER_OF_DAYS = (
    ('D1', '1 DAY'),
    ('D2', '2 DAY'),
    ('D3', '3 DAY'),
    ('D4', '4 DAY'),
    ('D5', '5 DAY'),
    ('D6', '6 DAY'),
    ('D7', '7 DAY'),
    ('D8', '8 DAY'),
    ('D9', '9 DAY'),
    ('D10', '10 DAY'),
    ('D11', '11 DAY'),
    ('D12', '12 DAY'),
    ('D13', '13 DAY'),
    ('D14', '14 DAY'),
    ('D15', '15 DAY'),
    ('D16', '16 DAY'),
    ('D17', '17 DAY'),
    ('D18', '18 DAY'),
    ('D19', '19 DAY'),
    ('D20', '20 DAY'),
    ('D21', '21 DAY'),
    ('D22', '22 DAY'),
    ('D23', '23 DAY'),
    ('D24', '24 DAY'),
    ('D25', '25 DAY'),
    ('D26', '26 DAY'),
    ('D27', '27 DAY'),
    ('D28', '28 DAY'),
    ('D29', '29 DAY'),
    ('D30', '30 DAY'),
    ('D31', '31 DAY'),
    ('D32', '32 DAY'),
    ('D33', '33 DAY'),
    ('D34', '34 DAY'),
    ('D35', '35 DAY'),
    ('D36', '36 DAY'),
    ('D37', '37 DAY'),
    ('D38', '38 DAY'),
    ('D39', '39 DAY'),
    ('D40', '40 DAY'),
    ('D41', '41 DAY'),
    ('D42', '42 DAY'),
    ('D43', '43 DAY'),
    ('D44', '44 DAY'),
    ('D45', '45 DAY'),
    ('D46', '46 DAY'),
    ('D47', '47 DAY'),
    ('D48', '48 DAY'),
    ('D49', '49 DAY'),
    ('D50', '50 DAY'),
    ('D51', '51 DAY'),
    ('D52', '52 DAY'),
    ('D53', '53 DAY'),
    ('D54', '54 DAY'),
    ('D55', '55 DAY'),
    ('D56', '56 DAY'),
    ('D57', '57 DAY'),
    ('D58', '58 DAY'),
    ('D58', '58 DAY'),
    ('D59', '59 DAY'),
    ('D60', '60 DAY'),
)

class FabricModel(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length = 100, unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
        
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)

    def get_absolute_url_edit(self):
        return reverse('fabric-edit', kwargs={'slug': self.slug})

    def get_absolute_url_delete(self):
        return reverse('fabric-delete', kwargs={'slug': self.slug})


class GarmentModel(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length = 100, unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
        
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)

    def get_absolute_url_edit(self):
        return reverse('garment-edit', kwargs={'slug': self.slug})

    def get_absolute_url_delete(self):
        return reverse('garment-delete', kwargs={'slug': self.slug})


COUPON_STATUS = (
    ('Valid', 'Valid'),
    ('Invalid', 'Invalid'),
)


class RandomCoupon(models.Model):
    code = models.CharField(max_length=8, null=True,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)     
    coupon_status = models.CharField(choices=COUPON_STATUS, max_length=10)                              

    def save(self, *args, **kwargs):
        r = random.randint(0,1000000000)
        self.code = str(r)
        super(RandomCoupon, self).save(*args, **kwargs)


Sizes_choices = (
    ('Small', 'Small'),
    ('Medium', 'Medium'),
    ('Large', 'Large'),
    ('XL', 'XL'),
    ('XXL', 'XXL'),
    ('XXXL', 'XXXL'),

)

class Size(models.Model):
    sizes = models.CharField(choices=Sizes_choices, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)     

    def __str__(self):
        return self.sizes


class ProductModel(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length = 100, unique=True, null=True, blank=True)
    category = models.ForeignKey(CategoryModel,on_delete=models.CASCADE,related_name='category')
    short_description = models.CharField(max_length=100)
    sale_price = models.CharField(max_length=3, null=True,default=0)
    item_fabric = models.ForeignKey(FabricModel,on_delete=models.CASCADE,related_name='fabric',null=True)
    sheila_included = models.BooleanField(default=False)
    product_in_demand = models.BooleanField(default=False)
    belt_included = models.BooleanField(default=False)
    garment_care = models.ForeignKey(GarmentModel,on_delete=models.CASCADE,related_name='garment',null=True)
    color = models.CharField(max_length=100,null=True)
    size = models.ForeignKey(Size,on_delete=models.CASCADE,related_name='size',null=True)
    quantity=models.IntegerField(default=1)
    sale_percentage = models.CharField(max_length=4, null=True,default=0)
    number_of_days = models.CharField(max_length=3)
    tags = models.CharField(max_length=100,null=True,blank=True)
    designer_note = models.CharField(max_length=500,null=True)
    total= models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
        
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)
    # def save_images(self,images):
    #     if images:
    #         for img in images:
    #             picture = ProductImgModel()
    #             picture.image = img
    def get_images(self):
        return ProductImgModel.objects.filter(product_id=self)

    def get_images_1(self):
        image = ProductImgModel.objects.filter(product_id=self)
        if image:
            img = image[0]
            if img:
                return img.image
            return None
        return None
    def get_images_2(self):
        image = ProductImgModel.objects.filter(product_id=self)
        if image:
            img = image[1]
            if img:
                return img.image
            return None
        return None
        
    def get_images_3(self):
        image = ProductImgModel.objects.filter(product_id=self)
        if image:
            img = image[3]
            if img:
                return img.image
            return None
        return None
    def get_sale_price(self,percentage):
        price = (self.total/100)*percentage
        sale = self.total - price
        self.sale_price = sale
        self.sale_percentage = percentage
        self.save()
        return self

    def get_absolute_url_delete(self):
        return reverse('product-delete', kwargs={'slug': self.slug})

    def get_absolute_url_edit(self):
        return reverse('product-edit', kwargs={'slug': self.slug})


    def get_absolute_url_sale_delete(self):
        return reverse('sale-delete', kwargs={'slug': self.slug})

    def get_absolute_url_sale_edit(self):
        return reverse('sale-edit', kwargs={'slug': self.slug})




class Coupon(models.Model):
    code = models.CharField(max_length=8, null=True,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)     
    coupon_status = models.CharField(choices=COUPON_STATUS, max_length=10)                              

    def __str__(self):
        return self.code

class ProductImgModel(models.Model):
    # title = models.CharField(max_length=100)
    product_id =  models.ForeignKey(ProductModel, on_delete=models.CASCADE ,related_name='images')
    image = models.ImageField(upload_to ="static/product/", blank=True )

    # def __str__(self):
    #     return self.image
    def get(self):
        return self.image
    def get_image(self):
        img = []
        for i in self.image:
            img.append[i]
        return img

class ProductDemandModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to ="static/product/", blank=True )

    # def __str__(self):
    #     return self.image
    def get(self):
        return self.title

class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    short_description = models.CharField(max_length=700)
    long_description = models.CharField(max_length=1400)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)


class SliderModel(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    image = models.ImageField(upload_to ="static/slider/", blank=True)
    description = models.CharField(max_length=250, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)


class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    email = models.EmailField(max_length=100)
    number = models.IntegerField()
    message = models.CharField(max_length=250, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value,)
        super().save(*args, **kwargs)


