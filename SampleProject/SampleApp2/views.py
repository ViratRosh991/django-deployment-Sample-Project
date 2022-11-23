from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def f33(req):
    return HttpResponse("<h1>Hello From SampleApp2 f33()</h1><hr />")
    
def f44(req):
    return HttpResponse("<h1>Hello From SampleApp2 f44()</h1><hr />")
    
#Creating Default-Home-Page***
def homepage(request):
    htmldata='''<center>
            <h1>Welcome To DEFAULT HOME-PAGE!!!</h1>
            <hr />
            <h2>Your Request Page-Is-Not-Found</h2>
            <hr />
            <h3>Plz Try Other URL or LINKS!!!</h3>
            <hr />
        </center>''';
    return HttpResponse(htmldata);