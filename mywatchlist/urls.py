from django.urls import path
from mywatchlist.views import show_mywatchlist, mywatchlist_xml, mywatchlist_json

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_mywatchlist, name='show_mywatchlist'),
    path('html/', show_mywatchlist, name='show_mywatchlist'),
    path('xml/', mywatchlist_xml, name='mywatchlist_xml'),
    path('json/', mywatchlist_json, name='mywatchlist_json'),
    # path('xml/<int:id>', mywatchlist_xml_by_id, name='mywatchlist_xml_by_id'),
    # path('json/<int:id>', mywatchlist_json_by_id, name='mywatchlist_json_by_id'),
]