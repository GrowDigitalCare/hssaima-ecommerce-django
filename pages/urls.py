from django.contrib import admin
from django.urls import path,include
from pages import views

urlpatterns = [
    path('',views.HomeView.as_view(),name="home-view"),
    path('shop/',views.ShopView.as_view(),name="shop-view"),
    path('checkout/',views.checkoutView.as_view(),name="shop-view"),

    path('privacy/',views.PrivacyView.as_view(),name="privacy-view"),
    path('refund/',views.RefundView.as_view(),name="refund-view"),
    path('terms/',views.TermView.as_view(),name="term-view"),
    path('contact/',views.ContactView.as_view(),name="contact-view"),
    path('about/',views.AboutView.as_view(),name="about-view"),

    path('category/<str:slug>',views.Product_by_categoy.as_view(),name="product_by_category"),

]
