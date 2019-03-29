# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from rest_framework import generics

from toi.forms import Level1Form
from toi.models import Level1, Level2, Level3
from toi.serializer import Level1serializer, Level2serializer, Level3serializer


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
    return render(request, 'news.html', context)


def videos(request):
    video = Level2.objects.filter(submenu__name='Videos')

    context = {
        'video': video
    }
    return render(request, 'videos.html', context)


def city(request):
    l3 = Level3.objects.all()

    context = {
        'l3': l3
    }
    return render(request, 'city.html', context)


def india(request):
    l3 = Level3.objects.all()

    context = {
        'l3': l3
    }
    return render(request, 'india.html', context)


def elections(request):
    l3 = Level3.objects.all()

    context = {
        'l3': l3
    }
    return render(request, 'elections.html', context)


def world(request):
    l3 = Level3.objects.all()

    context = {
        'l3': l3
    }
    return render(request, 'world.html', context)


def business(request):
    l3 = Level3.objects.all()

    context = {
        'l3': l3
    }
    return render(request, 'business.html', context)


def tech(request):
    l3 = Level3.objects.all()

    context = {
        'l3': l3
    }
    return render(request, 'tech.html', context)


def cricket(request):
    l3 = Level3.objects.all()

    context = {
        'l3': l3
    }
    return render(request, 'cricket.html', context)


def sports(request):
    l3 = Level3.objects.all()

    context = {
        'l3': l3
    }
    return render(request, 'sports.html', context)


def entertainment(request):
    l3 = Level3.objects.all()

    context = {
        'l3': l3
    }
    return render(request, 'entertainment.html', context)


def web_series(request):
    l3 = Level3.objects.all()

    context = {
        'l3': l3
    }
    return render(request, 'web-series.html', context)


def life_style(request):
    l3 = Level3.objects.all()

    context = {
        'l3': l3
    }
    return render(request, 'life-style.html', context)


def blogs(request):
    l3 = Level3.objects.all()

    context = {
        'l3': l3
    }
    return render(request, 'blogs.html', context)


def photos(request):
    l3 = Level3.objects.all()

    context = {
        'l3': l3
    }
    return render(request, 'photos.html', context)


def live_tv(request):
    l3 = Level3.objects.all()

    context = {
        'l3': l3
    }
    return render(request, 'live-tv.html', context)


def education(request):
    l3 = Level3.objects.all()

    context = {
        'l3': l3
    }
    return render(request, 'education.html', context)


def all_sections(request):
    l3 = Level3.objects.all()

    context = {
        'l3': l3
    }
    return render(request, 'all-sections.html', context)


# def base(request):
#     form = Level1Form()
#     return render(request, 'base.html', {'form': form})


class Level1CreateView(generics.ListCreateAPIView):
    serializer_class = Level1serializer
    queryset = Level1.objects.all()


class Level1RUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Level1serializer
    queryset = Level1.objects.all()


class Level1ListView(generics.ListAPIView):
    serializer_class = Level1serializer
    queryset = Level1.objects.all()


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


