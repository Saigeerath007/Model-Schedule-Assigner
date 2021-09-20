from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import NewUserForm, Preferences
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import TimeTable

seats = [-1, 2, 2, 2, 2, 2]
from django.http import HttpRequest


# Create your views here.


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("homepage")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="schedule_selector/Register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("homepage")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="schedule_selector/Login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("homepage")


@login_required(login_url='login')
def homepage(request):
    return render(request, 'schedule_selector/Home.html')


@login_required(login_url='login')
def preference(request):
    context = {}
    form = Preferences()
    context['form'] = form
    context['filled'] = False
    u = User.objects.get(username=request.user.username)
    try:
        t = TimeTable.objects.get(user=u)
        context['filled'] = True
    except:
        if request.method == 'POST':
            # POST, generate form with data from the request
            form = Preferences(request.POST)
            if form.is_valid():
                sch = -1
                p1 = form.cleaned_data['pref_1']
                p2 = form.cleaned_data['pref_2']
                p3 = form.cleaned_data['pref_3']
                p4 = form.cleaned_data['pref_4']
                p5 = form.cleaned_data['pref_5']
                print(p1, p2, p3, p4, p5)
                if request.user is not None:
                    l = [p1, p2, p3, p4, p5]
                    for i in l:
                        if seats[p1] > 0:
                            sch = p1
                            seats[p1] = seats[p1] - 1
                            break
                    s = ''
                    for i in l:
                        s = s + str(i) + ' '

                    u = User.objects.get(username=request.user.username)
                    try:
                        t = TimeTable(user=u, selected_pref=s, schedule=sch, schedule_assigned=True, pref_given=True)
                    except:
                        pass
                    print(s)
                    return redirect('homepage')
    return render(request, 'schedule_selector/Preference.html', context)
