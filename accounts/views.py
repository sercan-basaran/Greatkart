from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from .models import User
from .forms import UserForm
from django.contrib import messages


def registerUser(request):
    #kayıt olan kullanıları göstermek için admin panelinden de görebiliyoruz
    if request.method =="POST":
        print(request.POST)
        form=UserForm(request.POST)
        if form.is_valid():
            # password=form.cleaned_data['password']
            # user=form.save(commit=False)
            # #django'nun kendi şifreleme sistemini kullanıyor
            # user.set_password(password)
            # user.role=User.CUSTOMER
            # user.save()
            
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
            user.role=User.CUSTOMER
            user.save()
            print("user created")
            #form.save()
            messages.success(request,"Your account has been registered successfully!")
            return redirect("registerUser")
        else:
            print("form is not valid")
            print(form.errors)
    else:
       form=UserForm()
    context={
        "form":form
    } 
    return render (request,"accounts/registerUser.html",context)