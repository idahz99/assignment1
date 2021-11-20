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
    i = 0;
    current = datetime.datetime.now().year
    year = (People.objects.values_list('IcNo', flat=True))
    year2 = []
    for yeart in year:

        test = yeart[-4]
        if test == "0":
            print(yeart)
            year2.append(("20" + str(yeart)[:4]).replace(",", ""))
            print(year2)
        else:
            year2.append(("19" + str(yeart)[:4]).replace(",", ""))
            print(datetime.datetime.now().month)
    for getyear in year2:
        if datetime.datetime.now().month < int(year2[i][2:4]):
            print(int(year2[i][:4]))
            year2[i] = current - int(year2[i][:4])
            i += 1
        else:
            year2[i] = current - int(year2[i][:4])-1
            i +=1

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
