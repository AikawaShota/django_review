from django.shortcuts import render
from .forms import WineForm
import joblib
import numpy as np


def calc_wine(colorint, proline):
    loaded_model = joblib.load(open("finalized_rfc.sav", "rb"))
    x = np.array([colorint, proline])
    param = x.reshape(1, -1)
    pred = loaded_model.predict(param)
    return pred


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
