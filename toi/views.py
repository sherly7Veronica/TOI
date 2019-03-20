# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from toi.models import Level1, Level2, Level3
from toi.pagination import Pagination
from toi.serializer import Level1serializer, Level2serializer, Level3serializer
from rest_framework.response import Response


def home(request):
    return render(request, 'home.html')


def toi(request):
    l1 = Level1.objects.all()
    l2 = Level2.objects.all()
    l3 = Level3.objects.all()
    context = {
               'l1': l1,
               'l2': l2,
               'l3': l3
               }
    return render(request, 'menu.html', context)


class Level1CreateView(generics.ListCreateAPIView):
    serializer_class = Level1serializer
    queryset = Level1.objects.all()


class Level1RUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Level1serializer
    queryset = Level1.objects.all()


class Level1ListView(generics.ListAPIView):
    # pagination_class = Pagination
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'menu.html'
    serializer_class = Level1serializer
    queryset = Level1.objects.all()

    # def get(self, request):
    #     queryset = Level1.objects.all()
    #     return Response({'items': queryset})


class Level2CreateView(generics.ListCreateAPIView):
    serializer_class = Level2serializer
    queryset = Level2.objects.all()


class Level2RUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Level2serializer
    queryset = Level2.objects.all()


class Level2ListView(generics.ListAPIView):
    serializer_class = Level2serializer
    queryset = Level2.objects.all()


class Level3CreateView(generics.ListCreateAPIView):
    serializer_class = Level3serializer
    queryset = Level3.objects.all()


class Level3RUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Level3serializer
    queryset = Level3.objects.all()


class Level3ListView(generics.ListAPIView):
    serializer_class = Level3serializer
    queryset = Level3.objects.all()


