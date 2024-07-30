from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from book.models import Category, Book,Author
from book.serializers import (CategorySerializers,
                                BookSerialize,
                                AutherSerialize
                               )
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import ListAPIView

from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
class CategoryListView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def get(self,request):
        categories = Category.objects.all()
        serializers = CategorySerializers(categories,many=True,context= {'request':request })
        return Response(serializers.data,status=status.HTTP_200_OK)


class AuthorListView(APIView):
    def get(self,request):
        groups = Author.objects.all()
        serializers = AutherSerialize(groups, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

class BookListView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = BookSerialize
    # queryset = Book.objects.all()
    def get_queryset(self):
        queryset = Book.objects.select_related('category')
        return queryset
#
# class CategoryDelete(generics.DestroyAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = CategorySerializers
#     queryset = Category.objects.all()
#     lookup_field = 'pk'
#
# """ CRUD """

#
# class CategitiyListCRUD(generics.ListAPIView):
#     permission_classes = [IsAuthenticated]
#     model = Category
#     serializer_class = CategorySerializers
#     queryset = Category.objects.all()
#
# class BookList_CRUD(generics.ListAPIView):
#     model = Book
#     serializer_class = BookSerialize
#     queryset = Book.objects.all()
# class AutherList_CRUD(generics.ListAPIView):
#     model = Group
#     serializer_class = GroupModelSerialize
#     queryset = Group.objects.all()
#
#
# class CategoryDetialCRUD(generics.RetrieveAPIView):
#     model = Category
#     serializer_class = CustomersModelSerializers
#     lookup_field = 'pk'
#
#     def get_queryset(self):
#         queryset = Category.objects.all()
#         return queryset
#
# class CategoryAddCRUD(generics.CreateAPIView):
#     serializer_class = CustomersModelSerializers
#     queryset = Category.objects.all()
#
# class GroupAddCRUD(generics.CreateAPIView):
#     serializer_class = GroupModelSerialize
#     queryset = Group.objects.all()
#
# class ProductAddCRUD(generics.CreateAPIView):
#     serializer_class = ProductSerialize
#     queryset = Product.objects.all()
#
# class CategoryUpdata(generics.UpdateAPIView):
#     serializer_class = CustomersModelSerializers
#     queryset = Category.objects.all()
#     lookup_field = 'pk'
#
# class CategoryUpdata(generics.UpdateAPIView):
#     serializer_class = CustomersModelSerializers
#     queryset = Category.objects.all()
#     lookup_field = 'pk'
#
# class GroupUpdata(generics.UpdateAPIView):
#     serializer_class = GroupModelSerialize
#     queryset = Group.objects.all()
#     lookup_field = 'pk'
#
# class ProductUpdata(generics.UpdateAPIView):
#     serializer_class = ProductSerialize
#     queryset = Product.objects.all()
#     lookup_field = 'pk'
#
# class CategoryDelete(generics.DestroyAPIView):
#     serializer_class = CustomersModelSerializers
#     lookup_field = 'pk'
#     queryset = Category.objects.all()
# class GroupDelete(generics.DestroyAPIView):
#     serializer_class = GroupModelSerialize
#     lookup_field = 'pk'
#     queryset = Group.objects.all()
# class ProductDelete(generics.DestroyAPIView):
#     serializer_class = ProductSerialize
#     lookup_field = 'pk'
#     queryset = Product.objects.all()
#
# # """" ModelViewSet """
# class CategoryModelViewSet(viewsets.ModelViewSet):
#     serializer_class = CustomersModelSerializers
#     queryset = Category.objects.all()
#     lookup_field = 'pk'
#
# class GroupModelViewSet(viewsets.ModelViewSet):
#     serializer_class = GroupModelSerialize
#     queryset = Group.objects.all()
#     lookup_field = 'pk'
#
# class ProductModelViewSet(viewsets.ModelViewSet):
#     serializer_class = ProductSerialize
#     queryset = Product.objects.all()
#     lookup_field = 'pk'
