import datetime
from django import forms
from django.shortcuts import render

# Create your views here.

class FormName(forms.Form):
    task = forms.CharField(label="Name")
    # priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)

def index(request):
    now = datetime.datetime.now()
    return render(request, "WhoAreYou/index.html", {
        "newyear": now.month == 1 and now.day == 1
    })

# def greet1(request, name):
    return render(request, "WhoAreYou/greet.html", {
        "name": name.capitalize()
    })

def Home(request):
    return render(request, "WhoAreYou/Home.html")

def AboutUs(request):
    return render(request, "WhoAreYou/AboutUs.html")

def GameStudio(request):
    return render(request, "WhoAreYou/GameStudio.html")    


'''
def index(request):
    if request.method == "POST":
        form = FormName(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/index.html", {
                "form": form
            })
    else:
        return render(request, "tasks/index.html", {
            "form": FormName()
        })
'''