from django.shortcuts import render
from main.serializers import ProductSerializer
from main.models import Product
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import mixins
from rest_framework import generics
from rest_framework.parsers import MultiPartParser,FormParser

from django.views.generic import TemplateView,CreateView,UpdateView
from main.forms import ProductForm
from django.urls import reverse_lazy
# Create your views here.




class Products(APIView):
    model=Product
    serializer_class=ProductSerializer
    def get(self,request):
        products=self.model.objects.all()
        serializer=self.serializer_class(products,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






class ProductMixin(generics.GenericAPIView,mixins.ListModelMixin):
    parser_classes=[MultiPartParser,FormParser]
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self):
        pass


class ProductDetailMixin(generics.GenericAPIView,mixins.RetrieveModelMixin):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

class Home(TemplateView):
    template_name = "main/Home.html"

