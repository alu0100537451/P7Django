from django.shortcuts import render_to_response
from django.http import HttpResponse

# Create your views here.
 
def quick_test(request):
	return render_to_response("blog.html", {})

def test1(request):
        return render_to_response("home.html", {})

def test2(request):
        return render_to_response("help.html", {})

def test3(request):
        return render_to_response("about.html", {})


