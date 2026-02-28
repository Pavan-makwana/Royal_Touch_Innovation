from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('products/<slug:slug>/', views.product_detail, name="product_detail"),
    path('request/<int:id>/', views.request_product, name="request_product"),
    path('confirmation/', views.confirmation, name="confirmation"),
    path("request-success/", views.request_success, name="request_success"),
    path("privacy-policy/", views.privacy_policy, name="privacy_policy"),
    path("terms-and-conditions/", views.terms_conditions, name="terms_conditions"),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),




]
