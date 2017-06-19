from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from app.forms import APIForm
from django.urls import reverse_lazy
from app.api_function import api_lookup
from app.models import Entry
# Create your views here.

class IndexView(ListView):
    model = Entry 


def api_form_view(request):
    if request.method == "POST":
        r = request.POST
        form = APIForm(request.POST)
        if form.is_valid():
            api_lookup(r)
            return HttpResponseRedirect(reverse_lazy('index_view'))
    else:
        form = APIForm

    return render(request, 'api_entry.html', {'form': form})
