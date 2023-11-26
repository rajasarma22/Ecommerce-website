from django.shortcuts import render,redirect
from . models import*
from django.views.decorators.csrf import csrf_protect
# Create your views here.
def hi(request):
    return render(request,"home.html")

def data(request):
    fname = request.POST["fname"]
    lname = request.POST["lname"]
    email = request.POST["email"]
    contact = request.POST["contact"]
    password = request.POST["password"]

    n = mohan.objects.create(fistname=fname,lastname=lname,email=email,Contact=contact,password=password)
    return render(request,"two.html")
    #return redirect("showpage")

#def showpage(request):
   # all_data = mohan.objects.all()
   # return render(request,"two.html",{"key1":all_data})