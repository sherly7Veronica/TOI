# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from toi.models import Level1, Level2, Level3
from toi.pagination import Pagination
from toi.serializer import CategorySerializer
from rest_framework.response import Response


def home(request):
    return render(request, 'home.html')


def toi(request):
    queryset = Level1.objects.all()
    l2 = Level2.objects.all()
    l3 = Level3.objects.all()
    context = {
               'items': queryset,
               'l2': l2,
               'l3': l3
               }
    return render(request, 'menu.html', context)


class CategoryCreateView(generics.ListCreateAPIView):
    # pagination_class = Pagination
    serializer_class = CategorySerializer
    queryset = Level1.objects.all()


class CategoryRUDView(generics.RetrieveUpdateDestroyAPIView):
    # pagination_class = Pagination
    serializer_class = CategorySerializer
    queryset = Level1.objects.all()


class CategoryListView(generics.ListAPIView):
    # pagination_class = Pagination
    renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'menu.html'
    serializer_class = CategorySerializer
    queryset = Level1.objects.all()

    # def get(self, request):
    #     queryset = Level1.objects.all()
    #     return Response({'items': queryset})


# class Level2ListView(generics.ListAPIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     serializer_class = CategorySerializer
#     queryset = Level2.objects.all()


