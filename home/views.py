from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home (request):
    # return HttpResponse("""<h1>Hey i am a 
    #                     wvtlgnt
    # django server.</h1>""")
    # #use can use css as well

    return render(request, "home/index.html")  #returns not the response but the template 

def success_page(request):
    print("*" * 10)
    return HttpResponse("<h1> hey this is a success page </h1>")