from django.core.paginator import Paginator
from django.shortcuts import render
from listings.models import Game, Company
from listings.choices import category_choices


def index(request):
    games = Game.objects.order_by('-list_date')[:3]
    context = {
        'games': games,
        'category_choices': category_choices
    }
    return render(request, 'pages/index.html', context)


def about(request):
    companies = Company.objects.all()

    mvp_companies = Company.objects.all().filter(is_mvp=True)

    paginator = Paginator(companies, 3)
    page = request.GET.get('page')
    paged_companies = paginator.get_page(page)

    context = {
        'companies': paged_companies,
        'mvp_companies': mvp_companies
    }

    return render(request, 'pages/about.html', context)
