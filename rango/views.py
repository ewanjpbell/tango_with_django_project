from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    #Construct a dictionary to pass to the template engine as its context
    #Note the key boldmessage matches to the template
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    #Return a rendered response to send to the client.
    #Make use of the shortcurt function to make life easier
    #The first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict ={'boldmessage': 'This tutorial has been put together by Ewan Bell.'}
    
    return render(request, 'rango/about.html', context=context_dict)
