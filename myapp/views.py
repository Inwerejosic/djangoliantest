from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    path = request.path 
    method = request.method 
    x = 4
    v = 2
    y = x**v
    content=''' 
        <center><h2>Testing Django Request Response Objects</h2> 
        <p>Request path : " {}</p> 
        <p>Request Method :{}</p>
        <p style="color:tomato; font-style:italic">Request y : " {}</p></center> 
    '''.format(path, method, y) 
    return HttpResponse(content) 
    # return HttpResponse('<h1>Welcome to Little Lemon</h1>')
