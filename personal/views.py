from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from home.decorator import *
from inputdata.models import *
from django.http import JsonResponse


@login_required(login_url="login")
@allowed_user(allowed_roles=['admin'])
def personal(request):

    return render(request, "personal.html")


def update_personal(request):
    law = request.GET.get('law')
    department = request.GET.get('department')
    service = request.GET.get('service')

    if law == "Todos" and not service:
        list_personal = list(Personal.objects.all().values())
    elif law != "Todos" and not service:
        list_personal = list(Personal.objects.filter(is_pro=law).values())
    if law == "Todos" and not service and department == "Todos":
        list_personal = list(Personal.objects.all().values())
    elif law != "Todos" and not service and department == "Todos":
        list_personal = list(Personal.objects.filter(is_pro=law).values())
    elif department and law == "Todos" and not service:
        list_personal = list(Personal.objects.filter(service_id__department_id=department).values())
    elif department and law != "Todos" and not service:
        list_personal = list(Personal.objects.filter(service_id__department_id=department, is_pro=law).values())
    elif department and law == "Todos" and service == "Todos":
        list_personal = list(Personal.objects.filter(service_id__department_id=department).values())
    elif department and law != "Todos" and service == "Todos":
        list_personal = list(Personal.objects.filter(service_id__department_id=department, is_pro=law).values())
    elif service and law == "Todos":
        list_personal = list(Personal.objects.filter(service_id=service).values())
    elif service and law != "Todos":
        list_personal = list(Personal.objects.filter(service_id=service, is_pro=law).values())

    return JsonResponse({"list_personal": list_personal})


def data_personal(request):
    id_p = request.GET.get('id')
    p = Personal.objects.get(id=int(id_p))
    personal_data = list(Personal.objects.filter(id=int(id_p)).values())
    service = list(Service.objects.filter(id=p.service_id.id).values())
    s = Service.objects.get(id=p.service_id.id)
    department = list(Department.objects.filter(id=s.department_id.id).values())

    return JsonResponse({"personal_data": personal_data, "service": service, "department": department})


def get_licences(request):
    personal_id = request.GET.get('id')
    licenses = list(Licences.objects.all().values())
    lic = list(LicencesDates.objects.filter(personal_id=int(personal_id)).values())
    if lic:
        for l in lic:
            x = l['license_id_id']
            y = Licences.objects.get(id=int(x))
            l['license_id_id'] = y.name

    return JsonResponse({"licences": licenses, 'lic': lic})


def save_licenses(request):
    if request.method == 'POST':
        if request.is_ajax():

            from_date = request.POST['from']
            till_date = request.POST['till']
            personal_id = request.POST['personal_id']
            licences_id = request.POST['licences_id']
            print(from_date, till_date, personal_id, licences_id)

            p = Personal.objects.get(id=int(personal_id))
            l = Licences.objects.get(id=int(licences_id))

            if not LicencesDates.objects.filter(from_date=from_date, till_date=till_date, personal_id=p, license_id=l):

                licences = LicencesDates(
                    from_date=from_date,
                    till_date=till_date,
                    personal_id=p,
                    license_id=l
                )

                licences.save()

                success = 'La licencia se a registrado correctamente'
                return HttpResponse(success)

            else:

                success = 'La licencia ya existe'
                return HttpResponse(success)


def delete_licences(request):
    if request.method == 'POST':
        if request.is_ajax():

            id = request.POST['id']

            licences = LicencesDates.objects.get(id=int(id))
            licences.delete()

            success = 'La licencia ha sido eliminado correctamente'
            return HttpResponse(success)


