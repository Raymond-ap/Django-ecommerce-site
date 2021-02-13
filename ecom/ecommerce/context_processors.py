from .models import *


def globalData(request):
    daily_offers = DailyOffer.objects.all().order_by('-created')[0:1]

    return {
        'daily_offers': daily_offers
    }
