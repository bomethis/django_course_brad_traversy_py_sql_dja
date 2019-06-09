from django.shortcuts import render

from .models import Listing
listings = Listing.objects.all()


context = {
    'listings': listings
}


def index(request):
    return render(request, 'listings/listings.html', context)

def listing(request):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')
