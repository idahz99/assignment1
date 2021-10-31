from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse


def people(request):
    return render(request, 'App_Pkob/peopleInfo.html')

def penghulu(request):
    name = "zhamri che ani"
    village = "Merbok"
    return render(request, 'App_Pkob/Penghulu.html', context={'name': name, 'village': village})
   ## return HttpResponse("Hello zhamri")

from django.shortcuts import render


def peopleinfo_report(request):
    people_list = ["Ali", "Abu", "Ramli"]
    return render(request, 'App_Pkob/peopleInfo_report.html', context={'people_list': people_list})


