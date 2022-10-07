
from multiprocessing import context
from django.shortcuts import redirect, render
from vendor.forms import VendorForm
from .models import User, UserProfile
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


def registerVendor(request):
    if request.method=="POST":
        form=VendorForm(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
            user.role=User.VENDOR
            user.save()
            vendor=v_form.save(commit=False)
            vendor.user=user
            user_profile=UserProfile.objects.get(user=user)
            vendor.user_profile=user_profile
            vendor.save()
            print("vendor created")
            messages.success(request,"Your account has been registered successfully!")
            return redirect("registerVendor")
        else:
            print("form is not valid")
            print(form.errors)
    
    
    form=UserForm()
    v_form=VendorForm()
    
    context={
        'form':form,
        'v_form':v_form
    }
    
    return render(request,"accounts/registerVendor.html",context)