from django.shortcuts import render
from katalog.models import CatalogItem


# TODO: Create your views here.
def show_katalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = {
    'list_catalog': data_barang_katalog,
    'nama': 'Ied Mubaraque Sultan Salahuddine El Ayyubie',
    'id': '2106751120',
    }
    return render(request, "katalog.html", context)
    