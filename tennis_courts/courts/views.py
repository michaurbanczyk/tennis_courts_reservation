from django.shortcuts import render
from .models import Region, City


def home(request):
    return render(
        request,
        'base.html'
    )


def regions_view(request):
    all_regions = Region.objects.all()
    print("hello")
    return render(
        request,
        'courts/regions.html',
        {'all_regions': all_regions}
    )
