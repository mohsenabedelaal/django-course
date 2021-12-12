from django.shortcuts import redirect, render ,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already taken")
                # print("username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                # print("email taken")
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password1,
                    email=email,
                    first_name=first_name,
                    last_name=last_name
                )
                user.save()
                print("User Created")
                return redirect('/')
        else:
            messages.info(request,"password not matching...")
            # print("password not matching...")
            return redirect('register')
    else:
        return render(request,'register.html')