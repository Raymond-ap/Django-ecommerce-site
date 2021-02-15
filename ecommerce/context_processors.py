from django.shortcuts import render, redirect
from .models import *


def globalData(request):
    daily_offers = DailyOffer.objects.all().order_by('-created')[0:1]
    categories = Category.objects.all()[:15]


    return {
        'daily_offers': daily_offers,
        'categories': categories
    }


