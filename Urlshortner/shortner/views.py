from django.shortcuts import render
from django.http import HttpResponse
import uuid
from .models import Url

# Create your views here.


def index(request):
    return render(request, "index.html")


def create(request):
    if request.method == "POST":
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=link, uuid=uid)
        new_url.save()
        return HttpResponse(uid)
