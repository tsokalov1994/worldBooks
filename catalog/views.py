from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    text_head = "Header of main page"
    text_body = "Body of main page"
    context = {'text_head': text_head, 'text_body': text_body}
    return render(request, 'catalog/index.html', context)