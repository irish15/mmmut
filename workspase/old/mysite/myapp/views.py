from django.shortcuts import render
from .forms import PhotoForm

def index(req):
    if req.method == 'GET':
        return render(req, 'myapp/index.html', {
            'form': PhotoForm(),
        })
