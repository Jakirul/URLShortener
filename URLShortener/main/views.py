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
            url = form.cleaned_data.get('url')
            rand_number = randint(100, 99999)
            Main.objects.create(url=url, shortened_url=rand_number)
            return redirect("home")
    else:
        form = NewLinkForm()
    data = {'form': form, 'all': all}
    return render(request, "home.html", data)


def redirect_url(request, shortened_url):
    value = Main.objects.get(shortened_url=shortened_url)
    if value:
        return redirect(value.url)
    else:
        return render(request, "home.html")

