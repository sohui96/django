from secondapp.models import Hospital
# from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404

def index(request):
    return render(request, 'secondapp/index.html')

def hospital(request):
    hospital_list = Hospital.objects.all()
    print(hospital_list)

    return render(
        request, 'secondapp/hospital_list.html',
        {'hospital_list': hospital_list}
    )
