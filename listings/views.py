from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Game, Category
from companies.models import Company
from reviews.models import Review
from .choices import category_choices
from reviews.forms import ReviewForm
from django.contrib import messages


def index(request):
    games = Game.objects.all().filter(is_published=True)

    paginator = Paginator(games, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'games': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    game = get_object_or_404(Game, pk=listing_id)

    reviews = Review.objects.all().filter(game=game)

    form_review = ReviewForm()

    context = {
        'game': game,
        'reviews': reviews,
        'form': form_review
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Game.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(title__icontains=keywords)

    # Company
    if 'company' in request.GET:
        company = request.GET['company']
        if company:
            data = Company.objects.get(name__icontains=company)
            queryset_list = queryset_list.filter(author=data)

    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            data = Category.objects.get(title__icontains=category)
            queryset_list = queryset_list.filter(category=data)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            price = int(price)
            queryset_list = queryset_list.filter(price=price)

    context = {
        'games': queryset_list,
        'category_choices': category_choices
    }
    return render(request, 'listings/search.html', context)


def create_review(request):
    if request.method == 'POST':
        user = request.POST['user']
        game = request.POST['game']
        review = request.POST['review']
        id = request.POST['id']

        usr = User.objects.get(username=user)
        gm = Game.objects.get(title=game)

        create_rev = Review.objects.create(
            user=usr,
            game=gm,
            review=review
        )
        create_rev.save()
        messages.success(request, 'Your comment added')
        return redirect('listing', id)



