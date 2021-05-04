from django.shortcuts import render

from courts.models import Club


def home(request):
    return render(
        request,
        'courts/home.html'
    )


def clubs_view(request):
    all_clubs = Club.objects.all()
    return render(
        request,
        'courts/clubs.html',
        {'all_clubs': all_clubs}
    )
