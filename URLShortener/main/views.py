from django.shortcuts import render, redirect
from .models import Main
from .forms import NewLinkForm
from random import randint

# Create your views here.
def home(request):
    all = Main.objects.all()
    if request.method == 'POST':
        form = NewLinkForm(request.POST)
        if form.is_valid():
            rand_number = randint(100, 99999)
            url = form.cleaned_data.get('url')
            if not str(url).startswith("https"):
                Main.objects.create(url="https://"+url, shortened_url=rand_number)
            else:
                Main.objects.create(url=url, shortened_url=rand_number)
            
            return redirect("home")
    else:
        form = NewLinkForm()
    data = {'form': form, 'all': all}
    return render(request, "home.html", data)


def redirect_url(request, shortened_url):
    try:
        value = Main.objects.get(shortened_url=shortened_url)
        return redirect(value.url)
    except:
        return redirect("home")

