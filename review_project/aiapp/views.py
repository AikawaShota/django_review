from django.shortcuts import render
from .forms import WineForm
import pickle
import sklearn


def calc_wine(colorint, proline):
    rfc = pickle.load(open("finalized_rfc.sav", "rb"))
    wine = rfc.predict([[colorint, proline]])
    return wine


# Create your views here.
def index(request):
    form = WineForm()
    message = ""
    if request.method == "POST":
        form = WineForm(data=request.POST)
        if form.is_valid():
            colorint = float(request.POST["colorint"])
            proline = float(request.POST["proline"])
            wine = calc_wine(colorint, proline)
            message = f"ワインの種類は{wine[0]}です。"
            print("ok")
    context = {
        "form": form,
        "message": message
    }
    return render(request, 'aiapp/index.html', context)
