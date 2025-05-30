from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

def login(request):
    template_name = "login.html"
    message = ""

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            message = "Username atau password tidak boleh kosong!"
        else:
            user = authenticate(username=username, password=password)
            
            if user is not None:
                auth_login(request, user)
                return redirect("/")
            else:
                message = "Username atau password salah"

    context = {
        'title': 'Login',
        'message': message
    }

    return render(request, template_name, context)

def register(request):
    template_name = "register.html"
    message = ""

    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if not username or not first_name or not last_name or not password1 or not password2:
            message = "Input tidak boleh ada yang kosong!"
        else:
            if password1 != password2:
                message = "Password pertama dan kedua tidak cocok!"
            else:
                user = User.objects.filter(username=username)
                if user.exists():
                    message = "Username telah digunakan!"
                else:
                    if password1 != password2:
                        message = "Password pertama dan kedua tidak cocok!"
                    else:
                        if len(password1) < 8:
                            message = "Panjang password kurang dari 8"
                        else:
                            user = User.objects.create(
                            username = username,
                            first_name = first_name,
                            last_name = last_name
                            )
                            user.set_password(password1)
                            user.save()
                            return redirect("/")
                
    context = {
        'title': 'Registrasi',
        'message': message
    }

    return render(request, template_name, context)

def logout(request):
    auth_logout(request)
    return redirect("/")
