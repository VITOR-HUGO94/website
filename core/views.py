from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    front="""
    
    
    """
    return HttpResponse(front)

