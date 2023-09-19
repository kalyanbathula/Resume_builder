from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect


# Create your views here.
def index_view(request):
    return render(request, "index.html")


def jobs_view(request):
    return render(request, "jobs.html")


def contact_view(request):
    return render(request, "contact.html")


def tempsel_view(request):
    return render(request, "tempsel.html")


def companies_view(request):
    return render(request, "companies.html")


def template1_view(request):
    return render(request, "template1.html")


def template2_view(request):
    return render(request, "Newtemplate.html")


def template3_view(request):
    return render(request, "template3.html")


def JSD_view(request):
    return render(request, "JSD.html")


def JNSA_view(request):
    return render(request, "JNSA.html")


def JISA_view(request):
    return render(request, "JISA.html")


def JDBA_view(request):
    return render(request, "JDBA.html")


def JDS_view(request):
    return render(request, "JDS.html")


def JDART_view(request):
    return render(request, "JDART.html")


def JDALST_view(request):
    return render(request, "JDALST.html")


def JCSE_view(request):
    return render(request, "JCSE.html")


def formfinal_view(request):
    return render(request, "formfinal.html")


def JCA_view(request):
    return render(request, "JCA.html")


def JAI_view(request):
    return render(request, "JAI.html")


def video_view(request):
    return render(request, "video.html")


from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.


def SignupPage(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        email = request.POST.get("email")
        pass1 = request.POST.get("password1")
        pass2 = request.POST.get("password2")

        if pass1 != pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect("login")

    return render(request, "signup.html")


from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def LoginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        pass1 = request.POST.get("pass")
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            if (
                user.is_authenticated
            ):  # No need to check request.user.is_authenticated again
                login(request, user)
                request.session["username"] = username
                print("User authenticated and logged in successfully.")
                return redirect("profile")

        else:
            error_message = "Username or Password is incorrect!!!"
            return render(request, "login.html", {"error_message": error_message})

    return render(request, "login.html")


@login_required
def profile(request):
    username = request.session.get("username", None)
    if not username:
        print("Error: Username not found in session.")
        return redirect("login")
    else:
        print(f"Username '{username}' found in session.")
        return render(request, "tempsel.html", {"username": username})


@login_required
def jobs_view(request):
    username = request.session.get("username", None)
    return render(request, "jobs.html", {"username": username})


@login_required
def companies_view(request):
    username = request.session.get("username", None)
    return render(request, "companies.html", {"username": username})


from django.contrib.auth import logout
from django.shortcuts import redirect


def LogoutPage(request):
    logout(request)
    request.session.flush()  # Clear the session data and remove the session cookie
    return redirect("login")


# views.py

from django.shortcuts import render, HttpResponse
from .models import ContactFormEntry


def submit_form_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        comments = request.POST.get("comments")

        # Save form data to the database
        entry = ContactFormEntry.objects.create(
            name=name, email=email, phone=phone, comments=comments
        )
        entry.save()

        return HttpResponse("Form submitted successfully.")
    return HttpResponse("Invalid request method.")


def view_contact_form_entries(request):
    entries = ContactFormEntry.objects.all()
    return render(request, "view_entries.html", {"entries": entries})
