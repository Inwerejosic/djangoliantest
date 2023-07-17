from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # path = request.path 
    # method = request.method 
    # x = 4
    # v = 2
    # y = x**v
    # content= 
    # ''' 
    #     <center><h2>Testing Django Request Response Objects</h2> 
    #     <p>Request path : " {}</p> 
    #     <p>Request Method :{}</p>
    #     <p style="color:tomato; font-style:italic">Request y : " {}</p></center> 
    # '''.format(path, method, y) 
    # return HttpResponse(content) 
    return HttpResponse('<h1>Welcome to Little Lemon</h1>')

def drinks(request,): #drink_name):
    drink = {
        'mocha':'Type of Coffee',
        'tea':'Type of hot beverage',
        'lemonade':'Type of refreshment',
    }
    # choice_of_drink = drink[drink_name]
    zx_type = type(drink)
    # return HttpResponse(f"<h2>{drink_name}</h2> " + choice_of_drink)
    return HttpResponse(f"<h1>{zx_type}</h1>")

def about(request):
    return HttpResponse('<h1>About us</h1>')  


def menu(request):
    return HttpResponse('<h1>Menu</h1>')  


def book(request):
    return HttpResponse('<h1>Make a booking</h1>')    

def modify_str(request):
    str1 = 'I love Python'
    str2 = str1.replace("love", "enjoy").split()
    return HttpResponse(f"<center><h2>{str2}</h2></center>")
