from django.shortcuts import render,redirect
from .forms import Create_Form,Update_Form,Registration_Form,Login_Form
from .models import Create_Model
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def Create_View(req):
    form=Create_Form()
    context={}
    context["form"]=form
    if req.method=="POST":
        form=Create_Form(req.POST)
        if form.is_valid():
            book_name=form.cleaned_data.get("book_name")
            author=form.cleaned_data.get("author")
            language=form.cleaned_data.get("language")
            pages=form.cleaned_data.get("pages")
            price=form.cleaned_data.get("price")

            bkform=Create_Model(book_name=book_name,author=author,language=language,pages=pages,price=price)
            bkform.save()
            print("Saved")
            return redirect("listed")
    return render(req,"create.html",context)

def List_View(req):
    book=Create_Model.objects.all()
    context={}
    context["books"]=book
    return render(req,"list.html",context)

def Update_View(req,id):
    upda=Create_Model.objects.get(id=id)
    context={}
    form=Update_Form(instance=upda)
    context["form"]=form
    if req.method=="POST":
        form=Update_Form(instance=upda,data=req.POST)
        if form.is_valid():
            form.save()
            print("Updated")
            return redirect("listed")
    return render(req,"update.html",context)

def Delete_View(req,id):
    dele=Create_Model.objects.get(id=id)
    dele.delete()
    return redirect("listed")

def Registration_View(req):
    form=Registration_Form()
    context={}
    context["form"]=form
    if req.method=="POST":
        form=Registration_Form(req.POST)
        if form.is_valid():
            form.save()
            return redirect("loged")
        else:
            context["form"]=form
            return redirect("regised")
    return render(req,"register.html",context)

def Login_page(req):
    form=Login_Form()
    context={}
    context["form"]=form
    if req.method=="POST":
        form=Login_Form(req.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(req,username=username,password=password)
            if user:
                login(req,user)
                return redirect("home")
            else:
                context["form"]=form
                return render(req,"login.html",context)
    return render(req,"login.html",context)

def Home_Page(req):
    return render(req,"home.html")

def Logout(req):
    logout(req)
    return redirect("loged")
