from django.shortcuts import render, get_object_or_404

from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import bedroom_choices, state_choices, price_choices


# Create your views here. MVC framework - view rendering
def index(request):
    # Parse value to views
    listings = Listing.objects.all()

    paginator = Paginator(listings, 2)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html',
                  context)


# Set up paginator for listing
def listing(request, listing_id):
    _listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': _listing
    }
    return render(request, 'listings/listing.html',
                  context)


def search(request):
    query_list = Listing.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            """description__icontains searches for keyword matches within the item descriptions, 
            regardless of letter case."""
            query_list = query_list.filter(description__icontains=keywords)

    # Keywords
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            query_list = query_list.filter(city__icontains=city)

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            """ Filter the query_list to include items matching the specified city"""
            query_list = query_list.filter(state__exact=state)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            """Filter the query_list to include items with a number of bedrooms less than or equal to the specified 
            value"""
            query_list = query_list.filter(bedrooms__lte=bedrooms)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            query_list = query_list.filter(price__lte=price)

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': query_list,
        'values': request.GET  # preserve form input
    }
    return render(request, 'listings/search.html',
                  context
                  )
