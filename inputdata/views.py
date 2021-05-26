from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from inputdata.models import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from home.decorator import *
import datetime
from django.db.models import Q
from datetime import timedelta
import requests
from calendar import monthrange, month_name, day_name


@allowed_user(allowed_roles=['admin'])
@login_required(login_url="login")
def input_data(request):
    return render(request, "input_data.html")

# -------------------------------------##### JAVASCRIPT REQUESTS ##### --------------------------------------------

# --------------------------------------------GET DEPARTMENTS------------------------------------------------


def get_departments(request):
    department_list = list(Department.objects.values())
    return JsonResponse({"department_list": department_list})


# ----------------------------------------GET DEPARTMENTS EDIT------------------------------------------------


def get_department_edit(request):
    selected_id = request.GET.get('selDepartment')

    department = list(Department.objects.filter(id=selected_id).values())

    return JsonResponse({"department": department})

# ------------------------------------------SAVE DEPARTMENTS------------------------------------------------


def create_department(request):
    if request.method == 'POST':
        if request.is_ajax():
            if "dep_name" in request.POST:
                name = request.POST['dep_name']

                if not Department.objects.filter(name=name):
                    section = Department(
                        name=name,
                    )

                    section.save()

                    success = 'El departamento '+name+' se ha registrado correctamente'
                    return HttpResponse(success)

                else:
                    error = 'El departamento '+name+' no se ha registrado correctamente'
                    return HttpResponse(error)

# -------------------------------------------------EDIT DEPARTMENTS------------------------------------------------


def update_department(request):
    if request.method == 'POST':
        if request.is_ajax():

            name = request.POST['dep_name']
            id = request.POST['id']

            if id != "":

                department = Department.objects.get(id=id)
                department.name = name

                department.save()

                success = 'El departamento ' + name + ' se ha actualizado correctamente'
                return HttpResponse(success)
            else:
                error = 'El departamento ' + name + ' no existe o no fue seleccionado de la lista'
                return HttpResponse(error)

# ------------------------------------------------DELETE DEPARTMENT------------------------------------------------


def delete_department(request):
    if request.method == 'POST':
        if request.is_ajax():

            id = request.POST['id']

            department = Department.objects.get(id=id)
            department.delete()

            success = 'El departamento ha sido eliminado correctamente'
            return HttpResponse(success)

# ------------------------------------------GET SERVICE------------------------------------------------


def get_service(request):
    selected_department = request.GET.get('selDepartment')
    obj_services = list(Service.objects.filter(department_id=selected_department).values())
    return JsonResponse({"service_list": obj_services})

# -------------------------------------GET SERVICE EDIT------------------------------------------------


def get_service_edit(request):
    selected_id = request.GET.get('selService')

    service = list(Service.objects.filter(id=selected_id).values())

    return JsonResponse({"service":service})

# --------------------------------------SAVE SERVICE------------------------------------------------


def create_service(request):
    if request.method == 'POST':
        if request.is_ajax():
            if "sname" in request.POST:
                department = request.POST['department']
                name = request.POST['sname']
                id_hc = Department.objects.get(id=department)
                if not Service.objects.filter(name=name, department_id=id_hc):
                    service = Service(
                        name=name,
                        department_id=id_hc
                    )

                    service.save()

                    success = 'El servicio '+name+' se ha registrado correctamente'
                    return HttpResponse(success)

                else:
                    error = 'El servicio '+name+' no se ha registrado correctamente'
                    return HttpResponse(error)


# -------------------------------------------------EDIT SERVICE------------------------------------------------


def update_service(request):
    if request.method == 'POST':
        if request.is_ajax():
            department = request.POST['department']
            name = request.POST['sname']
            id = request.POST['id']
            print(department)
            if id != "":

                id_h = Department.objects.get(id=department)
                service = Service.objects.get(id=id)
                service.department_id = id_h
                service.name = name

                service.save()

                success = 'El servicio ' + name + ' se ha actualizado correctamente'
                return HttpResponse(success)
            else:
                error = 'El servicio ' + name + ' no existe o no fue seleccionada de la lista'
                return HttpResponse(error)


# -----------------------------------------DELETE SERVICE------------------------------------------------


def delete_service(request):
    if request.method == 'POST':
        if request.is_ajax():

            id = request.POST['id']

            service = Service.objects.get(id=id)
            service.delete()

            success = 'El servicio ha sido eliminado correctamente'
            return HttpResponse(success)

# ---------------------------------------------GET GUARDS------------------------------------------------


def get_guard(request):

    selected_service = request.GET.get('selServ')
    id_h = Service.objects.get(id=selected_service)
    obj_guard = list(Guard.objects.filter(service_id=id_h).values())
    return JsonResponse({"guards": obj_guard})

# ---------------------------------------------GET GUARD EDIT------------------------------------------------


def get_guard_edit(request):
    selected_id = request.GET.get('selGuard')
    guard = list(Guard.objects.filter(id=selected_id).values())
    return JsonResponse({"guard": guard})

# -----------------------------------------------SAVE GUARD------------------------------------------------


def create_guard(request):
    if request.method == 'POST':
        if request.is_ajax():
            if "duration" in request.POST:
                service_sel = request.POST['service']
                name = request.POST['name']
                g_type = request.POST['type']
                duration = request.POST['duration']
                id_h = Service.objects.get(id=service_sel)

                if not Guard.objects.filter(name=name, service_id=id_h):
                    guard = Guard(
                        name=name,
                        type=g_type,
                        duration_hs=duration,
                        service_id=id_h
                    )

                    guard.save()

                    success = 'La guardia / turno '+name+' se ha registrado correctamente'
                    return HttpResponse(success)

                else:
                    error = 'La guardia / turno '+name+' no se ha registrado correctamente'
                    return HttpResponse(error)


# ---------------------------------------------------EDIT GUARD------------------------------------------------


def update_guard(request):
    if request.method == 'POST':
        if request.is_ajax():
            service = request.POST['service']
            name = request.POST['name']
            g_type = request.POST['type']
            duration = request.POST['duration']
            id_g = request.POST['id']
            if id != "":

                id_h = Service.objects.get(id=service)
                guard = Guard.objects.get(id=id_g)
                guard.category_id = id_h
                guard.name = name
                guard.type = g_type
                guard.duration_hs = duration

                guard.save()

                success = 'La guardia/turno ' + name + ' se ha actualizado correctamente'
                return HttpResponse(success)
            else:
                error = 'La guardia/turno ' + name + ' no existe o no fue seleccionada de la lista'
                return HttpResponse(error)


# ----------------------------------------------------DELETE GUARD------------------------------------------------


def delete_guard(request):
    if request.method == 'POST':
        if request.is_ajax():

            id_g = request.POST['id']

            guard = Guard.objects.get(id=id_g)
            guard.delete()

            success = 'El registro ha sido eliminado correctamente'
            return HttpResponse(success)


# -------------------------------------------------GET PERSONAL------------------------------------------------


def get_personal(request):
    selected_service = request.GET.get('selSer')
    id_h = Service.objects.get(id=selected_service)
    obj_personal = list(Personal.objects.filter(service_id=id_h, is_active="yes").values())
    return JsonResponse({"personal": obj_personal})

# -------------------------------------------GET PERSONAL EDIT------------------------------------------------


def get_personal_edit(request):
    selected_id = request.GET.get('selPer')
    person = list(Personal.objects.filter(id=selected_id).values())

    return JsonResponse({"person": person})


# -----------------------------------------------SAVE PERSONAL------------------------------------------------


def create_personal(request):
    if request.method == 'POST':
        if request.is_ajax():

            service = request.POST['service']
            file = request.POST['file']
            d = request.POST['d']
            names = request.POST['name']
            last_n = request.POST['last_name']
            profession = request.POST['profession']
            phone = request.POST['phone']
            is_pro = request.POST['is_pro']

            if Service.objects.get(id=service):
                id_h = Service.objects.get(id=service)

                if not Personal.objects.filter(last_name=last_n, service_id=id_h, phone=phone):
                    persona = Personal(
                        file=file,
                        d=d,
                        name=names,
                        last_name=last_n,
                        profession=profession,
                        phone=phone,
                        service_id=id_h,
                        is_pro=is_pro
                    )

                    persona.save()

                    idp = Personal.objects.get(last_name=last_n, service_id=id_h, phone=phone)
                    password = file
                    user = Account(
                        username=phone,
                        personal_id=idp,

                    )
                    user.set_password(password)
                    user.save()

                    if is_pro == "true":
                        g = Group.objects.get(name='1904')
                        user.groups.add(g)

                    else:
                        g = Group.objects.get(name='1844')
                        user.groups.add(g)

                    success = 'La persona '+last_n+', '+name+' se ha registrado correctamente'
                    return HttpResponse(success)

                else:
                    error = 'La persona ' + last_n + ', ' + name + ' ya existe en este servicio'
                    return HttpResponse(error)
            else:
                errorc = 'Seleccione sector y categoria de la persona'
                return HttpResponse(errorc)


# -------------------------------------------------EDIT PERSONAL------------------------------------------------


def update_personal(request):
    if request.method == 'POST':
        if request.is_ajax():
            category = request.POST['service']
            file = request.POST['file']
            d = request.POST['d']
            name = request.POST['name']
            last_n = request.POST['last_name']
            profession = request.POST['profession']
            phone = request.POST['phone']
            is_pro = request.POST['is_pro']
            id = request.POST['id']
            if id != "":

                id_h = Service.objects.get(id=category)
                person = Personal.objects.get(id=id)
                person.category_id = id_h
                person.file = file
                person.d = d
                person.name = name
                person.last_name = last_n
                person.profession = profession
                person.phone = phone
                person.is_pro = is_pro

                person.save()

                success = 'La persona ' + last_n + ', ' + name + ' se ha actualizado correctamente'
                return HttpResponse(success)
            else:
                error = 'La persona ' + last_n + ', ' + name + ' no existe o no fue seleccionada de la lista'
                return HttpResponse(error)


# -------------------------------------------------DELETE PERSONAL------------------------------------------------


def delete_personal(request):
    if request.method == 'POST':
        if request.is_ajax():

            id = request.POST['id']
            persona = Personal.objects.get(id=int(id))
            persona.delete()

            success = 'El registro ha sido eliminado correctamente'
            return HttpResponse(success)

# --------------------------------------------GET NOT WORKING DAYS------------------------------------------------


def get_notworking(request):
    now = datetime.datetime.today()
    print(now)
    notworking = list(NotWorkingDays.objects.filter(Q(date__gte=now)|Q(date=None)).values())
    return JsonResponse({"notworking": notworking})


# ----------------------------------------GET NOT WORKING DAYS EDIT------------------------------------------------


def get_notworking_edit(request):
    selected_id = request.GET.get('selNotWorking')

    notworking = list(NotWorkingDays.objects.filter(id=selected_id).values())

    return JsonResponse({"notworking": notworking})

# ------------------------------------------SAVE NOT WORKING DAYS------------------------------------------------


def create_notworking(request):
    if request.method == 'POST':
        if request.is_ajax():
            if "w_name" in request.POST:
                name = request.POST['w_name']
                date = request.POST['date']

                if not NotWorkingDays.objects.filter(name=name):
                    notworking = NotWorkingDays(
                        date=date,
                        name=name,
                    )

                    notworking.save()

                    success = 'El feriado '+name+' se ha registrado correctamente'
                    return HttpResponse(success)

                else:
                    error = 'El feriado '+name+' no se ha registrado correctamente'
                    return HttpResponse(error)

# ----------------------------------------------EDIT NOT WORKING DAYS------------------------------------------------


def update_notworking(request):
    if request.method == 'POST':
        if request.is_ajax():

            name = request.POST['w_name']
            date = request.POST['date']
            id = request.POST['id']

            if id != "":

                notworking = NotWorkingDays.objects.get(id=id)
                notworking.name = name
                notworking.date = date

                notworking.save()

                success = 'El feriado ' + name + ' se ha actualizado correctamente'
                return HttpResponse(success)
            else:
                error = 'El feriado ' + name + ' no existe o no fue seleccionado de la lista'
                return HttpResponse(error)

# ----------------------------------------------DELETE NOT WORKING DAYS----------------------------------------------


def delete_notworking(request):
    if request.method == 'POST':
        if request.is_ajax():

            id = request.POST['id']

            notworking = NotWorkingDays.objects.get(id=id)
            notworking.delete()

            success = 'El feriado ha sido eliminado correctamente'
            return HttpResponse(success)

# --------------------------------------------GET LICENCE------------------------------------------------


def get_licences(request):
    licences = list(Licences.objects.values())
    return JsonResponse({"licences": licences})


# ----------------------------------------GET LICENCE EDIT------------------------------------------------


def get_licences_edit(request):
    selected_id = request.GET.get('selLicences')

    licences = list(Licences.objects.filter(id=selected_id).values())

    return JsonResponse({"licences": licences})

# ------------------------------------------SAVE LICENCE------------------------------------------------


def create_licences(request):
    if request.method == 'POST':
        if request.is_ajax():
            if "name" in request.POST:
                name = request.POST['name']
                print(name)

                if not Licences.objects.filter(name=name):
                    licences = Licences(
                        name=name,
                    )

                    licences.save()

                    success = 'La licencia '+name+' se ha registrado correctamente'
                    return HttpResponse(success)

                else:
                    error = 'La licencia '+name+' no se ha registrado correctamente'
                    return HttpResponse(error)

# ----------------------------------------------EDIT LICENCE------------------------------------------------


def update_licences(request):
    if request.method == 'POST':
        if request.is_ajax():

            name = request.POST['name']
            id = request.POST['id']

            if id != "":

                licences = Licences.objects.get(id=id)
                licences.name = name

                licences.save()

                success = 'La licencia ' + name + ' se ha actualizado correctamente'
                return HttpResponse(success)
            else:
                error = 'La licencia ' + name + ' no existe o no fue seleccionado de la lista'
                return HttpResponse(error)

# ----------------------------------------------DELETE LICENCE----------------------------------------------


def delete_licences(request):
    if request.method == 'POST':
        if request.is_ajax():

            id = request.POST['id']

            licences = Licences.objects.get(id=id)
            licences.delete()

            success = 'La licencia ha sido eliminado correctamente'
            return HttpResponse(success)

# --------------------------------------------GET POINTS------------------------------------------------


def get_points(request):
    points = list(Points.objects.values())
    return JsonResponse({"points": points})


# ----------------------------------------GET POINTS EDIT------------------------------------------------


def get_points_edit(request):
    selected_id = request.GET.get('selPoints')

    points = list(Points.objects.filter(id=selected_id).values())

    return JsonResponse({"points": points})

# ------------------------------------------SAVE POINTS------------------------------------------------


def create_points(request):
    if request.method == 'POST':
        if request.is_ajax():
            if "type" in request.POST:
                typep = request.POST['type']
                day = request.POST['day']
                point = request.POST['points']

                if not Points.objects.filter(points=point):
                    points = Points(
                        type=typep,
                        day=day,
                        points=point,
                    )

                    points.save()

                    success = 'El puntaje se ha registrado correctamente'
                    return HttpResponse(success)

                else:
                    error = 'El puntaje no se ha registrado correctamente'
                    return HttpResponse(error)

# ----------------------------------------------EDIT POINTS------------------------------------------------


def update_points(request):
    if request.method == 'POST':
        if request.is_ajax():

            typep = request.POST['type']
            day = request.POST['day']
            point = request.POST['points']
            id = request.POST['id']

            if id != "":

                points = Points.objects.get(id=id)
                points.type = typep
                points.day = day
                points.points = point

                points.save()

                success = 'El puntaje se ha actualizado correctamente'
                return HttpResponse(success)
            else:
                error = 'El puntaje no existe o no fue seleccionado de la lista'
                return HttpResponse(error)

# ----------------------------------------------DELETE POINTS----------------------------------------------


def delete_points(request):
    if request.method == 'POST':
        if request.is_ajax():

            id = request.POST['id']

            points = Points.objects.get(id=id)
            points.delete()

            success = 'El puntaje ha sido eliminado correctamente'
            return HttpResponse(success)













