from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import json
# Create your views here.

def Home(request):
    return render(request, 'SnifferServer/GUI.html')

def History(request):

    f = open(r"D:\Mina\Term 8\Computer Networks\packet-sniffer\sniffed_pkts.json")
    data = json.load(f)
    f.close()
    
    return render(request, 'SnifferServer/GUI.html', {
        'data' : data
    })