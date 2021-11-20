import datetime

from .models import People
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.


from django.http import HttpResponse


def people(request, ic):

    person = People.objects.get(IcNo=ic)
    return render(request, 'App_Pkob/peopleInfo.html', context={'person': person})


def penghulu(request):
    name = "zhamri che ani"
    village = "Merbok"
    return render(request, 'App_Pkob/Penghulu.html', context={'name': name, 'village': village})


def peopleinfo_report(request):
    current = datetime.datetime.now().year
    year = (People.objects.values_list('IcNo'))

    year2= [("19"+ str(acyear)[:4]).replace("('","") for acyear in year]

    year2[:] = [current - int(getyear) for getyear in year2]
    print(year2);
    year2.reverse()
    print(year2);
    people_list = People.objects.all()
    print(people_list);
    return render(request, 'App_Pkob/peopleInfo_report.html', context={'people_list': people_list, "year2": year2})


def edit(request):
    if request.method == "POST":
        person = People.objects.get(IcNo=request.POST['icNo'])
        person.Phone = request.POST['pNum']
        person.save()
        return redirect('peopleinfo')
    else:
        print("not successfull")


def register(request):
    if request.method == 'POST':
        print(request.POST)

        full_name = request.POST['fullname']
        ic = request.POST['icNo']
        phone_num = request.POST['pNum']
        if People.objects.filter(IcNo=ic).exists():

            messages.info(request, 'Person identity card number already exist in the system')
            return redirect('register')
        else:
            people_ = People.objects.create(IcNo=ic, Name=full_name, Phone=phone_num)
            people_.save()

        return redirect('register')

    else:
        return render(request, 'App_Pkob/Register.html')
