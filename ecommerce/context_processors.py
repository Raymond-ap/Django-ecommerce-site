from django.shortcuts import render, redirect
from .models import *


def globalData(request):
    daily_offers = DailyOffer.objects.all().order_by('-created')[0:1]
    categories = Category.objects.all()[:15]
    totalCost = 0
    
    if request.user.is_authenticated:
        items = OrderItem.objects.filter(
            user=request.user).order_by('-created')
        totalCost = 0
        # Calculating total cost
        for item in items:
            totalCost += item.getTotalPrice
    else:
        items = []

    return {
        'daily_offers': daily_offers,
        'categories': categories,
        "items": items,
        'totalCost': totalCost,
    }
