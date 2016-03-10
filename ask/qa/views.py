from django.shortcuts import render
from django.http import HttpResponse

def test(req, *args, **kwargs):
    return HttpResponse("OK")

