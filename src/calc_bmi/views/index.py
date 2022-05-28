from django.shortcuts import render

from calc_bmi.forms import UploadImageForm
from calc_bmi.models import Predict

# Create your views here.
def index(request):
    params = {
        'upload_form': UploadImageForm()
    }

    if (request.method == 'POST'):
        upload_image = Predict(
            image=request.FILES['target'],
            result=1
        )
        upload_image.save()

    return render(request, 'index.html', params)
