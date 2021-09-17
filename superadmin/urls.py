from django.contrib import admin
from django.urls import path,include
from superadmin import views

urlpatterns = [
    path('',views.MyDashboardView.as_view(),name="dashboard"),

    path('category/',views.CategoryView.as_view(),name="category-view"),
    path('category/add',views.CategoryViewForm.as_view(),name="category-form"),
    # ******** Category_Edit_Delete **********
    path('categor/<str:slug>/',views.update_view,name="category-edit"),
    path('catego/<str:slug>/',views.CategoryDelete.as_view(),name="category-delete"),


    # ******** Category_Edit_Delete **********

    path('size/',views.sizeView.as_view(),name="size-view"),
    path('size/add',views.sizeViewForm.as_view(),name="size-form"),


    path('product/<str:slug>/',views.ProductView.as_view(),name="product-edit"),
    path('product/<str:slug>/',views.ProductDeleteView.as_view(),name="product-delete"),

    path('product/',views.ProductView.as_view(),name="product-view"),
    path('product/add',views.ProductViewForm.as_view() ,name="product-form"),

    path('fabric/',views.FabricView.as_view(),name="fabric-view"),
    path('fabric/add',views.FabricViewForm.as_view() ,name="fabric-form"),
    path('fabric_delete/<str:slug>/',views.FabricDelete.as_view(),name="fabric-delete"),
    path('fabric_edit/<str:slug>/',views.update_fabric,name="fabric-edit"),


    path('garment/',views.GarmentView.as_view(),name="garment-view"),
    path('garment/add',views.GarmentViewForm.as_view() ,name="garment-form"),
    path('garment_delete/<str:slug>/',views.GarmentDelete.as_view(),name="garment-delete"),
    path('garment_edit/<str:slug>/',views.update_garment,name="garment-edit"),

    # ******** Garment_Edit_Delete **********

    path('garment/<str:slug>/',views.GarmentView.as_view(),name="garment-edit"),
    path('garment/<str:slug>/',views.GarmentViewForm.as_view(),name="garment-delete"),

    # ******** Garment_Edit_Delete **********



    path('order/',views.OrderView.as_view(),name="order-view"),

    path('sales/',views.ProductSaleView.as_view(),name="sales-view"),
    path('sale/add/',views.SaleView.as_view(),name="sale-form"),
    path('sale/<str:slug>/',views.SaleDeleteView.as_view(),name="sale-delete"),
    path('sale/<str:slug>/',views.SaleEditView.as_view(),name="sale-edit"),
    # path('order/',views.OrderView.as_view(),name="order-form"),

    path('blog/',views.BlogView.as_view(),name="blog-view"),
    path('blog/add',views.BlogViewForm.as_view(),name="blog-form"),
    path('blog_delete/<str:slug>/',views.BlogDelete.as_view(),name="blog-delete"),
    path('blog_edit/<str:slug>/',views.update_blog,name="blog-edit"),

    path('slider/',views.SliderView.as_view(),name="slider-view"),
    path('slider/add',views.SliderViewForm.as_view(),name="slider-form"),
    path('slider_delete/<str:slug>/',views.SliderDelete.as_view(),name="slider-delete"),
    path('slider_edit/<str:slug>/',views.update_slider,name="slider-edit"),


]
