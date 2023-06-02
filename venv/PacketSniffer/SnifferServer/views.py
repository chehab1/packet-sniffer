from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import json
# Create your views here.

def Home(request):
    return render(request, 'SnifferServer/GUI.html')

def History(request):
    with open("sniffed_pkts.json", 'r') as file:
            json_data = file.read()

    response = HttpResponse(json_data, content_type='application/json')
    response['Content-Disposition'] = f'attachment; filename=sniffed_pkts.json'
    return response