from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import MyWatchList

# Create your views here.

def show_mywatchlist(request):
    data_film = MyWatchList.objects.all()

    film_watched = 0
    film_not_watched = 0

    for films in data_film :
        if (films.watched):
            film_watched += 1
        else:
            film_not_watched += 1

    if (film_watched >= film_not_watched):
        context = {
        'list_film' : data_film,
        'bonus' : "Selamat, kamu sudah banyak menonton!",
        'sum_watched' : film_watched,
        'sum_not_watched' : film_not_watched
        }
    else :
        context = {
        'list_film' : data_film,
        'bonus' : "Wah, kamu masih sedikit menonton!",
        'sum_watched' : film_watched,
        'sum_not_watched' : film_not_watched
        }
    return render(request, "mywatchlist.html", context)

def mywatchlist_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def mywatchlist_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# def mywatchlist_xml_by_id(request, id):
#     data = MyWatchList.objects.filter(pk=id)
#     return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# def mywatchlist_json_by_id(request, id):
#     data = MyWatchList.objects.filter(pk=id)
#     return HttpResponse(serializers.serialize("json", data), content_type="application/json")