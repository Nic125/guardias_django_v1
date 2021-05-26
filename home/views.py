from django.db import transaction
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from calendar import monthrange, month_name, day_name
import dateutil.relativedelta
from inputdata.models import *
from home.decorator import *
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from home.serializer import *


@login_required(login_url="login")
@allowed_user(allowed_roles=['admin'])
def home(request):
    guards = Guard.objects.all()
    departments = Department.objects.all()
    this_month = datetime.datetime.now()
    last_month = this_month + dateutil.relativedelta.relativedelta(months=-1)
    this_month_db = str(this_month.year) + " " + str(this_month.month)
    last_month_db = str(last_month.year) + " " + str(last_month.month)
    mrange = monthrange(int(this_month.year), int(this_month.month))
    last_mrange = monthrange(int(last_month.year), int(last_month.month))
    month_range = mrange
    last_m_n = month_name[int(last_month.month)]
    last_month_n = last_m_n.capitalize()
    previous_month_name = month_name[last_month.month]
    not_workind_days = NotWorkingDays.objects.filter(date__year=this_month.year)
    l_days = []
    last_l_days =[]

    colors = ['#66bfbf', '#f76b8a', '#28df99', '#1687a7', '#557174', '#9dad7f', '#ffe268', '#ffb037', '#2f5d62',
              '#810000', '#ce1212', '#150e56', '#e2703a', '#864000', '#93329e', '#f14668', '#a1cae2', '#ffe227',
              '#944e6c', '#120078']

    for day in range(1, mrange[1] + 1):
        x = datetime.date(int(this_month.year), int(this_month.month), day).isoweekday()
        date = str(this_month.year) + "-" + str(this_month.month).zfill(2) + "-" + str(day).zfill(2)
        date_db = datetime.date.fromisoformat(date)

        y = [str(day).zfill(2), day_name[x - 1]]
        if x == 6 or x == 7:
            y.append("Fin de semana")
            y.append(day)
            l_days.append(y)
        else:
            dw = ""
            if len(not_workind_days) != 0:
                for dates in not_workind_days:
                    if date_db == dates.date:
                        dw = "No hábil"
                    else:
                        if dw != "No hábil":
                            dw = "Hábil"
            else:
                dw = "Hábil"
            y.append(dw)
            y.append(day)
            l_days.append(y)

    list_days = l_days

    current_month_guards = []

    guardl=[]
    for d in range(1, mrange[1] + 1):
        x = datetime.date(int(this_month.year), int(this_month.month), d).isoweekday()
        date = str(this_month.year) + "-" + str(this_month.month).zfill(2) + "-" + str(d).zfill(2)
        date_db = datetime.date.fromisoformat(date)

        y = [str(d).zfill(2), day_name[x - 1]]
        if x == 6:
            y.append("Sábado")
        elif x == 7:
            y.append("Domingo")
        else:
            dw = ""
            if len(not_workind_days) != 0:
                for dates in not_workind_days:
                    if date_db == dates.date:
                        dw = "No hábil"
                    else:
                        if dw != "No hábil":
                            dw = "Hábil"
            else:
                dw = "Hábil"
            y.append(dw)

        date = str(this_month.year) + "-" + str(this_month.month).zfill(2) + "-" + str(d).zfill(2)
        date_db = datetime.date.fromisoformat(date)
        day = []
        g = []
        for guard in guards:
            day_guard = GuardSheet.objects.filter(guard_id=guard.id, date=date_db)
            g.append(day_guard)
            y.append(g)
        guardl.append(y)


        cont = 0
    current_month_guards.append(guardl)

    for day in range(1, last_mrange[1] + 1):
        x = datetime.date(int(last_month.year), int(last_month.month), day).isoweekday()
        date = str(last_month.year) + "-" + str(last_month.month).zfill(2) + "-" + str(day).zfill(2)
        date_db = datetime.date.fromisoformat(date)

        y = [str(day).zfill(2), day_name[x - 1]]
        if x == 6 or x == 7:
            y.append("Fin de semana")
            y.append(day)
            l_days.append(y)
        else:
            dw = ""
            if len(not_workind_days) != 0:
                for dates in not_workind_days:
                    if date_db == dates.date:
                        dw = "No hábil"
                    else:
                        if dw != "No hábil":
                            dw = "Hábil"
            else:
                dw = "Hábil"
            y.append(dw)
            y.append(day)
            last_l_days.append(y)

    last_list_days = last_l_days


    previous_month_guards = []
    guardl = []
    for d in range(1, last_mrange[1] + 1):
        x = datetime.date(int(last_month.year), int(last_month.month), d).isoweekday()
        date = str(last_month.year) + "-" + str(last_month.month).zfill(2) + "-" + str(d).zfill(2)
        date_db = datetime.date.fromisoformat(date)

        y = [str(d).zfill(2), day_name[x - 1]]
        if x == 6:
            y.append("Sábado")
        elif x == 7:
            y.append("Domingo")
        else:
            dw = ""
            if len(not_workind_days) != 0:
                for dates in not_workind_days:
                    if date_db == dates.date:
                        dw = "No hábil"
                    else:
                        if dw != "No hábil":
                            dw = "Hábil"
            else:
                dw = "Hábil"
            y.append(dw)

        date = str(last_month.year) + "-" + str(last_month.month).zfill(2) + "-" + str(d).zfill(2)
        date_db = datetime.date.fromisoformat(date)
        day = []
        g = []
        for guard in guards:
            day_guard = GuardSheet.objects.filter(guard_id=guard.id, date=date_db)
            g.append(day_guard)
            y.append(g)
        guardl.append(y)

        cont = 0
    previous_month_guards.append(guardl)

    return render(request, "home.html", {'list_days': list_days, 'last_list_days': last_list_days,
                                         'departments': departments, 'current_month_guard': current_month_guards,
                                         'previous_month_guards': previous_month_guards, 'pmn': previous_month_name,
                                         'last_month_name': last_month_n})


def get_guards(request):
    date = request.GET.get('date')
    guard_id = request.GET.get('guard_id')
    guards = GuardSheet.objects.filter(date=date, guard_id=guard_id)
    guards_serializer = GuardsheetsSerializer(guards, many=True)
    return JsonResponse(guards_serializer.data, safe=False)

# --------------------------------------SAVE GUARD------------------------------------------------


def create_guard_entry(request):
    if request.method == 'POST':
        if request.is_ajax():
            if "guard_id" in request.POST:
                guard_id = request.POST['guard_id']
                date = request.POST['date']
                month_year = request.POST['month_year']
                is_working_day = request.POST['is_working_day']
                personal_id = request.POST['personal_id']
                shift = request.POST['shift']
                shift_day = request.POST['shift_day']
                hours = request.POST['hours']
                is_extra = request.POST['is_extra']
                is_active = request.POST['is_active']

                shift_day_d = ""
                if len(shift_day) < 1:
                    shift_day_d = "Turno mañana"
                else:
                    shift_day_d = shift_day

                active = "pasiva"
                if is_active == "activa":
                    active = "activa"

                id_g = Guard.objects.get(id=int(guard_id))
                id_p = Personal.objects.get(id=int(personal_id))

                if shift == "24" or shift == "12":
                    guard = GuardSheet(
                        date=date,
                        month_year=month_year,
                        is_working_day=is_working_day,
                        is_active=active,
                        shift=shift,
                        guard_id=id_g,
                        personal_id=id_p,
                        )

                    guard.save()

                else:
                    if is_extra == "yes":
                        guard = GuardSheet(
                            date=date,
                            month_year=month_year,
                            is_working_day=is_working_day,
                            shift=shift_day_d,
                            is_extra=hours,
                            guard_id=id_g,
                            personal_id=id_p,
                        )

                        guard.save()
                    else:
                        guard = GuardSheet(
                            date=date,
                            month_year=month_year,
                            is_working_day=is_working_day,
                            shift=shift_day_d,
                            guard_id=id_g,
                            personal_id=id_p,
                        )

                        guard.save()

                success = 'El servicio  se ha registrado correctamente'
                return HttpResponse(success)

# -------------------------------------------------EDIT GUARD------------------------------------------------


def update_guard_entry(request):
    if request.method == 'POST':
        if request.is_ajax():
            id_guardsheet = request.POST['id']
            guard_id = request.POST['guard_id']
            personal_id = request.POST['personal_id']
            shift = request.POST['shift']
            shift_day = request.POST['shift_day']
            hours = request.POST['hours']
            is_extra = request.POST['is_extra']
            is_active = request.POST['is_active']
            print(guard_id)
            shift_day_d = ""
            if len(shift_day) < 1:
                shift_day_d = "Turno mañana"
            else:
                shift_day_d = shift_day

            if shift == "24" or shift == "12":
                guard_d = GuardSheet.objects.get(id=id_guardsheet)
                id_p = Personal.objects.get(id=int(personal_id))
                print(guard_d.id, id_p.id)
                guard_d.is_active = is_active
                guard_d.personal_id = id_p
                guard_d.save()
                transaction.commit()

            else:
                if is_extra == "yes":
                    guard = GuardSheet.objects.get(id=id_guardsheet)
                    id_p = Personal.objects.get(id=int(personal_id))
                    guard.shift = shift_day_d
                    guard.is_extra = hours
                    guard.personal_id = id_p
                    guard.save()
                else:
                    guard = GuardSheet.objects.get(id=id_guardsheet)
                    id_p = Personal.objects.get(id=int(personal_id))
                    guard.shift = shift_day_d
                    guard.is_extra = "no"
                    guard.personal_id = id_p
                    guard.save()

            success = 'El servicio  se ha registrado correctamente'
            return HttpResponse(success)

# --------------GET GUARD EDIT------------------------------------------


def get_guard(request):
    guard_id = request.GET.get('selGuard')
    guard = GuardSheet.objects.get(id=int(guard_id))
    guard_serializer = GuardsheetsSerializer(guard)
    return JsonResponse(guard_serializer.data)


# --------------DELETE GUARD------------------------------------------


def delete_guard(request):
    if request.method == 'GET':
        if request.is_ajax():

            guard_id = request.GET.get('selGuard')
            guard = GuardSheet.objects.get(id=int(guard_id))
            guard.delete()

            success = 'El registro ha sido eliminado correctamente'
            return HttpResponse(success)