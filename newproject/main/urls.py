from django.urls import path
from main import views

urlpatterns=[
    path("products/",views.ProductMixin.as_view()),
    path("products/<int:pk>",views.ProductDetailMixin.as_view()),
    path("",views.Home.as_view()),
    path("products/add",views.CreateProduct.as_view())
]