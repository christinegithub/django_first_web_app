from random import randint
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def root(request):
    return HttpResponseRedirect('home')

def gallery_page(request):
    return HttpResponseRedirect('../portfolio')

def home_page(request):
    context = {'name': 'Betty Maker'}
    response = render(request, 'index.html', context)
    return HttpResponse(response)

def portfolio_page(request):

    image_urls = []
    for i in range(5):
        random_number = randint(0,100)
        image_urls.append("https://picsum.photos/400/600/?image={}".format(random_number))


    context = {'gallery_images': image_urls}
    response = render(request, 'gallery.html', context)
    return HttpResponse(response)

def about_me_page(request):
    skills = ['html', 'css', 'python']
    interests = ['dance', 'travel']

    context = {'skills': skills, 'interests': interests}
    response = render(request, 'about_me.html', context)
    return HttpResponse(response)

def favourites_page(request):

    fave_links = ["https://www.google.com/", "https://www.facebook.com/"]
    context = {'links': fave_links}
    response = render(request, 'favourites.html', context)
    return HttpResponse(response)
