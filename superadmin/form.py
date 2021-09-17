from django.forms import fields, widgets
from superadmin import models
from django import forms


Sizes = (
    ('Small', 'Small'),
    ('Medium', 'Medium'),
    ('Large', 'Large'),
    ('XL', 'XL'),
    ('XXL', 'XXL'),
    ('XXXL', 'XXXL'),
    ('Custom', (
            ('Item Length', 'Item Length'),
            ('Hips', 'Hips'),
            ('Neck Size', 'Neck Size'),
            ('Shoulder Size', 'Shoulder Size'),
            ('Waist', 'Waist'),
            ('Sleeves Width', 'Sleeves Width'),
            ('Sleeves from Neck', 'Sleeves from Neck'),
            ('Sleeves from Shoulder', 'Sleeves from Shoulder'),
            ('Shirt Length', 'Shirt Length'),
            ('Trouser Length', 'Trouser Length'),
            ('Upper Arm Width', 'Upper Arm Width'),

        )
    ),
)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.CategoryModel
        fields = ['title','image']
        widgets={
            'title': forms.TextInput(attrs={'class':"form-control", 'name':"firstname", 'placeholder':"First name"}),
        }

class BlogForm(forms.ModelForm):
    class Meta:
        model = models.BlogModel
        fields = ['title','short_description','long_description']
        widgets={
            'title': forms.TextInput(attrs={'class':"form-control", 'name':"firstname", 'placeholder':"First name"}),
        }


class SliderForm(forms.ModelForm):
    class Meta:
        model = models.SliderModel
        fields = ['title','image','description']
        widgets={
            'title': forms.TextInput(attrs={'class':"form-control", 'name':"firstname", 'placeholder':"First name"}),
        }

class sizeForm(forms.ModelForm):
    class Meta:
        model = models.Size
        fields = ['sizes']
        widgets={
            'sizes': forms.TextInput(attrs={'class':"form-control", 'name':"sizes", 'placeholder':"Size"}),
        }

class GarmentForm(forms.ModelForm):
    class Meta:
        model = models.GarmentModel
        fields = ['title']
        widgets={
            'title': forms.TextInput(attrs={'class':"form-control", 'name':"firstname", 'placeholder':"First name"}),
        }

class FabricForm(forms.ModelForm):
    class Meta:
        model = models.FabricModel
        fields = ['title']
        widgets={
            'title': forms.TextInput(attrs={'class':"form-control", 'name':"firstname", 'placeholder':"First name"}),
        }



class ProductForm(forms.ModelForm):
    class Meta:
        model = models.ProductModel
        # fields = ['__all__']
        size = forms.ChoiceField(choices = Sizes, label="", initial='', widget=forms.Select(), required=True)

        fields=['title','category','short_description','sale_price','item_fabric','sheila_included','belt_included','garment_care','color','size','quantity','number_of_days','tags','designer_note']
        widgets={
            'title': forms.TextInput(attrs={'class':"form-control", 'name':"firstname", 'placeholder':"First name"}),
            # 'category': forms.
            # 'category': forms.ChoiceField(attrs={'class':"form-control", 'name':"firstname", 'placeholder':"First name"}),
        }

class ProductDemandForm(forms.ModelForm):
    class Meta:
        model = models.ProductDemandModel
        # fields = ['__all__']
        fields=['title','image']
        widgets={
            'title': forms.TextInput(attrs={'class':"form-control", 'name':"title", 'placeholder':"Title"}),
            # 'category': forms.
            # 'category': forms.ChoiceField(attrs={'class':"form-control", 'name':"firstname", 'placeholder':"First name"}),
        }


class BlogForm(forms.ModelForm):
    class Meta:
        model = models.BlogModel
        fields = ['title','short_description','long_description']
        widgets={
            'title': forms.TextInput(attrs={'class':"form-control", 'name':"firstname", 'placeholder':"First name"}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.ContactModel
        fields = ['name','email','number','message']
        widgets={
            'title': forms.TextInput(attrs={'class':"form-control", 'name':"firstname", 'placeholder':"First name"}),
        }
