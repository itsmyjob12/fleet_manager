from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group

def login_view(request):
    from .forms import LoginForm  # Importer à l'intérieur de la fonction
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.groups.filter(name='Administrateurs').exists():
                    return redirect("/")  # Rediriger vers l'interface administrateur
                elif user.groups.filter(name='Conducteurs').exists():
                    return redirect("/driver-dashboard/")  # Rediriger vers l'interface conducteur
                else:
                    return redirect("/")  # Rediriger vers une page par défaut si l'utilisateur n'appartient à aucun groupe
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})
                

def password_change_view(request):
    from .forms import SignUpForm  # Importer à l'intérieur de la fonction
    msg = None
    success = False

    if request.method == "PUT":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data.get("role")

            if role == 'admin':
                admin_group, created = Group.objects.get_or_create(name='Administrateurs')
                admin_group.user_set.add(user)
            elif role == 'driver':
                driver_group, created = Group.objects.get_or_create(name='Conducteurs')
                driver_group.user_set.add(user)

            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect("/login/")
            else:
                msg = 'Authentication failed.'
        else:
            msg = 'Form is not valid: ' + str(form.errors)
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})




def admin_dashboard(request):
    # Logic for admin dashboard
    return render(request, 'accounts/admin_dashboard.html')

def driver_dashboard(request):
    # Logic for driver dashboard
    return render(request, 'accounts/driver_dashboard.html')
