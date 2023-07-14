from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import Search
from django.contrib.messages import constants
from django.contrib import messages
from .useful import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

def do_search(request):
    if request.method == 'POST':
        url = request.POST.get('search')

        page_count = 40
        urls = bing_search(url, page_count)
        relevant_urls = get_relevant_links(urls)

        date = datetime.now()

        links_search = Search(
            link=url,
            links_list=relevant_urls,
            date=date,
        )

        links_search.save()

        return redirect('/search/search_done')
    
def search_done(request):
    last_search = Search.objects.latest('id')

    context = {
        'link_list': last_search.links_list
    }

    return render(request, 'search_done.html', context)

def history(request):
    date_filter = request.GET.get('date_filter')

    if date_filter == 'all':
        search_results = Search.objects.all().order_by('-date')
    elif date_filter:
        try:
            selected_date = datetime.strptime(date_filter, '%B %d, %Y').strftime('%Y-%m-%d')
            search_results = Search.objects.filter(date=selected_date).order_by('-date')
        except ValueError:
            search_results = []
    else:
        search_results = []

    dates = Search.objects.values_list('date', flat=True).distinct().order_by('-date')

    context = {
        'search_results': search_results,
        'dates': dates,
    }
    return render(request, 'history.html', context)

def delete_history(request, id):
    history_item = Search.objects.get(id=id)
    history_item.delete()
    messages.add_message(request, constants.ERROR, 'ITEM has been DELETED')
    return redirect('/search/history/?date_filter=all')

def access_search(request, id):
    search = Search.objects.get(id=id)
    link = search.link
    links_list = search.links_list

    context = {
        'link':link,
        'links_list':links_list,
    }

    return render(request, 'access_search.html', context)