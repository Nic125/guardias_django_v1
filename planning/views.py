from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from inputdata.models import *
import datetime
from calendar import monthrange, month_name
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import locale
from django.http import JsonResponse
from django.utils.datastructures import MultiValueDictKeyError
from home.decorator import *
import dateutil.relativedelta

locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')
list_days = []
month_range = 0
year_sel = 0
month_sel = 0
guard_sel = ""
number_personal = 0


@allowed_user(allowed_roles=['admin'])
@login_required(login_url="login")
def sheets_data(request):
    global list_days, month_range, year_sel, month_sel, guard_sel, number_personal
    departments = Department.objects.all()
    guards = Guard.objects.all()
    this_month = datetime.datetime.now()
    last_month = this_month + dateutil.relativedelta.relativedelta(months=-1)
    next_month = this_month + dateutil.relativedelta.relativedelta(months=+1)
    this_month_db = str(this_month.year) + " " + str(this_month.month)
    last_month_db = str(last_month.year) + " " + str(last_month.month)
    next_month_db = str(next_month.year) + " " + str(next_month.month)
    this_month_op = str(this_month.year) + "-" + str(this_month.month)
    last_month_op = str(last_month.year) + "-" + str(last_month.month)
    next_month_op = str(next_month.year) + "-" + str(next_month.month)
    this_month_range = monthrange(int(this_month.year), int(this_month.month))
    last_month_range = monthrange(int(last_month.year), int(last_month.month))
    previous_month_name = month_name[last_month.month]
    not_workind_days = NotWorkingDays.objects.filter(date__year=this_month.year)

    months_list = [last_month_op, month_name[last_month.month], this_month_op, month_name[this_month.month],
                   next_month_op, month_name[next_month.month]]

    day_name = ['LUN', 'MAR', 'MIÉ', 'JUE', 'VIE', 'SÁB', 'DOM']

# --------CURRENT MONTH GUARDS---------------------

    current_month_guards = []
    for guard in guards:
        current_month_name = month_name[int(this_month.month)]
        g = []
        g.append(current_month_name)
        g.append(guard.id)
        g.append(guard.name)
        g.append(guard.service_id.department_id.name)
        days = []
        for d in range(1, this_month_range[1] + 1):
            day = []
            x = datetime.date(int(this_month.year), int(this_month.month), d).isoweekday()
            date = str(this_month.year) + "-" + str(this_month.month).zfill(2) + "-" + str(d).zfill(2)
            date_db = datetime.date.fromisoformat(date)
            day.append(str(d).zfill(2))
            day.append(day_name[int(x) - 1])
            dw = ""
            for dates in not_workind_days:

                if date_db == dates.date:
                    if dw != "Feriado":
                        dw = "Feriado"
                else:
                    if dw != "Feriado":
                        if day_name[int(x) - 1] == "SÁB":
                            dw = "SÁB"
                        elif day_name[int(x) - 1] == "DOM":
                            dw = "DOM"
                        else:
                            dw = "Hábil"
            day.append(dw)
            day_guard = GuardSheet.objects.filter(guard_id=guard.id, date=date_db, month_year=this_month_db)
            day.append(day_guard)
            days.append(day)
            g.append(days)

        current_month_guards.append(g)

# --------LAST MONTH GUARDS---------------------

    previous_month_guards = []
    for guard in guards:
        last_month_name = month_name[int(last_month.month)]
        g = []
        g.append(last_month_name)
        g.append(guard.id)
        g.append(guard.name)
        g.append(guard.service_id.department_id.name)
        days = []
        for d in range(1, last_month_range[1] + 1):
            day = []
            x = datetime.date(int(last_month.year), int(last_month.month), d).isoweekday()
            date = str(last_month.year) + "-" + str(last_month.month).zfill(2) + "-" + str(d).zfill(2)
            date_db = datetime.date.fromisoformat(date)
            day.append(str(d).zfill(2))
            day.append(day_name[int(x) - 1])
            dw = ""
            for dates in not_workind_days:

                if date_db == dates.date:
                    if dw != "Feriado":
                        dw = "Feriado"
                else:
                    if dw != "Feriado":
                        if day_name[int(x) - 1] == "SÁB":
                            dw = "SÁB"
                        elif day_name[int(x) - 1] == "DOM":
                            dw = "DOM"
                        else:
                            dw = "Hábil"
            day.append(dw)
            if GuardSheet.objects.filter(guard_id=guard.id, date=date_db, month_year=last_month_db):
                day_guard = GuardSheet.objects.filter(guard_id=guard.id, date=date_db, month_year=last_month_db)
                day.append(day_guard)
            days.append(day)
            g.append(days)

        previous_month_guards.append(g)


# ------------------------- UPDATE -----------------------------------

    if request.method == "POST":
        if "actualizar" in request.POST:
            m = request.POST['month']
            dep = request.POST['department']
            ser = request.POST['service']
            guard = request.POST['selected_guard_menu']
            guard_sel = guard
            personal = Personal.objects.filter(service_id=ser, is_active="yes")
            all_personal = Personal.objects.filter(service_id__department_id=dep, is_active="yes")
            guard_s = Guard.objects.get(id=guard)
            year, mo = m.split("-")
            not_workind_days = NotWorkingDays.objects.filter(date__year=year)

            if guard_s.type == "pasiva":
                pasive = "pasiva"
            else:
                pasive = "activa"
            if int(guard_s.duration_hs) > 8:

                year_s = year
                year_sel = year_s
                month = mo.lstrip("0")
                month_s = month
                month_sel = month_s
                mrange = monthrange(int(year), int(month))
                month_range = mrange
                month_n = month_name[int(month)]
                l_days = []
                month_year = str(year_s) + " " + str(month_s)


                for day in range(1, mrange[1] + 1):
                    x = datetime.date(int(year), int(month), day).isoweekday()
                    date = str(year_sel) + "-" + str(month_sel).zfill(2) + "-" + str(day).zfill(2)
                    date_db = datetime.date.fromisoformat(date)

                    y = [str(day).zfill(2), day_name[x - 1]]
                    if x == 6:
                        y.append("Sábado")
                        y.append(day)

                    elif x == 7:
                        y.append("Domingo")
                        y.append(day)
                    else:
                        dw = ""
                        for dates in not_workind_days:
                            if date_db == dates.date:
                                dw = "No hábil"
                            else:
                                if dw != "No hábil":
                                    dw = "Hábil"
                        y.append(dw)
                        y.append(day)
                    try:
                        day_guard = GuardSheet.objects.filter(date=date_db, guard_id=guard_s.id)
                        is_in_day = []
                        for day1 in day_guard:
                            is_in_day.append(day1.personal_id.id)
                        y.append(is_in_day)
                    except:
                        day_guard = False
                    l_days.append(y)

                list_days = l_days

                return render(request, "planning.html",
                              {"l_days": l_days, "month": month_n, "year": year, 'guardm': guard_s,
                               'personal': personal, 'departments': departments, 'pasive':pasive,
                               'month_list': months_list})


# ------------------------------------ MULTIPLE GUARDS --------------------------------------------------------

            elif int(guard_s.duration_hs) == 8:

                year, mo = m.split("-")
                year_s = year
                year_sel = year_s
                month = mo.lstrip("0")
                month_s = month
                month_sel = month_s
                mrange = monthrange(int(year), int(month))
                month_range = mrange
                month_n = month_name[int(month)]
                guard_s = Guard.objects.get(id=guard)
                l_days = []

                id_h = Guard.objects.get(name=guard_s, service_id=ser)
                month_year = str(year_s) + " " + str(month_s)

                for day in range(1, mrange[1] + 1):
                    date = str(year_sel) + "-" + str(month_sel).zfill(2) + "-" + str(day).zfill(2)
                    date_db = datetime.date.fromisoformat(date)
                    x = datetime.date(int(year), int(month), day).isoweekday()

                    y = [str(day).zfill(2), day_name[x - 1]]
                    if x == 6:
                        y.append("Sábado")
                        y.append(day)
                        l_days.append(y)
                    elif x == 7:
                        y.append("Domingo")
                        y.append(day)
                        l_days.append(y)
                    else:
                        dw = ""
                        for dates in not_workind_days:
                            if date_db == dates.date:
                                dw = "No hábil"
                            else:
                                if dw != "No hábil":
                                    dw = "Hábil"
                        y.append(dw)
                        y.append(day)
                    try:
                        day_guard = GuardSheet.objects.filter(date=date_db, guard_id=guard_s.id, shift="Turno mañana")
                        is_in_day = []
                        for day1 in day_guard:
                            is_in_day.append(day1.personal_id.id)
                            if day1.is_extra != "no":
                                is_in_day.append("yes")
                        y.append(is_in_day)
                    except:
                        day_guard = False
                        is_in = [0]
                        y.append(is_in)
                    try:
                        day_guard = GuardSheet.objects.filter(date=date_db, guard_id=guard_s.id, shift="Turno tarde")
                        is_in_day = []
                        for day1 in day_guard:
                            is_in_day.append(day1.personal_id.id)
                            if day1.is_extra != "no":
                                is_in_day.append("yes")
                        y.append(is_in_day)
                    except:
                        day_guard = False
                        is_in1 = [0]
                        y.append(is_in1)
                    try:
                        day_guard = GuardSheet.objects.filter(date=date_db, guard_id=guard_s.id, shift="Turno noche")
                        is_in_day = []
                        for day1 in day_guard:
                            is_in_day.append(day1.personal_id.id)
                            if day1.is_extra != "no":
                                is_in_day.append("yes")
                        y.append(is_in_day)
                    except:
                        day_guard = False
                        is_in2 = [0]
                        y.append(is_in2)

                    l_days.append(y)

                list_days = l_days

                return render(request, "planning.html",
                              {"multiple_days": l_days, "month": month_n, "year": year,
                                'guardm': guard_s, 'personal': personal,
                               'departments': departments, 'pasive': pasive, 'month_list': months_list})


# ------------------------------------ SAVE GUARDS 24HS --------------------------------------------------------

    if request.method == 'POST':
        if "guardar_guardias" in request.POST:
            sel_guard_id = request.POST['selected_guard_id']
            guard_selected = Guard.objects.get(id=int(sel_guard_id))
            service_id = guard_selected.service_id
            month_year = str(year_sel) + " " + str(month_sel)
            personal_service = Personal.objects.filter(service_id=service_id, is_active="yes")
            try:
                guards_replace = GuardSheet.objects.filter(month_year=month_year,
                                                           guard_id=guard_selected.id)
                for g in guards_replace:
                    g.delete()
            except guards_replace.DoesNotExist:
                guards_replace = None

            for person in personal_service:
                for day in range(1, int(month_range[1]) + 1):
                    date = str(year_sel) + "-" + str(month_sel).zfill(2) + "-" + str(day).zfill(2)
                    date_db = datetime.date.fromisoformat(date)
                    month_year = str(year_sel) + " " + str(month_sel)
                    is_working_day = request.POST['workd' + str(person.id) + "d" + str(day)]
                    person_id = request.POST['m' + str(person.id) + "d" + str(day)]


                    try:
                        is_selected = request.POST["select_day" + str(person.id) + "d" + str(day)]
                        if is_selected == "on":

                            if int(person_id) == person.id:
                                guard = GuardSheet(
                                    date=date_db,
                                    month_year=month_year,
                                    is_working_day=is_working_day,
                                    is_active=guard_selected.type,
                                    guard_id=guard_selected,
                                    personal_id=person,
                                )

                                guard.save()

                    except MultiValueDictKeyError:
                        is_selected = False

                month_n = month_name[int(month_sel)]

            messages.error(request,
                           f"La planilla del correspondiente a {month_n} de {year_sel} a sido almacenada correctamente")
            return render(request, "planning.html", {'departments': departments,
                                                     'current_month_guard': current_month_guards,
                                                     'previous_month_guards': previous_month_guards,
                                                     'pmn': previous_month_name,
                                                     'month_list': months_list})

# ------------------------------------ SAVE MULTIPLE GUARDS --------------------------------------------------------

    if request.method == 'POST':
        if "multiple_guards" in request.POST:
            sel_guard_id = request.POST['selected_guard_id']
            guard_selected = Guard.objects.get(id=int(sel_guard_id))
            service_id = guard_selected.service_id
            month_year = str(year_sel) + " " + str(month_sel)
            personal_service = Personal.objects.filter(service_id=service_id, is_active="yes")
            try:
                guards_replace = GuardSheet.objects.filter(month_year=month_year,
                                                           guard_id=guard_selected.id)
                for g in guards_replace:
                    g.delete()
            except guards_replace.DoesNotExist:
                guards_replace = None

            for person in personal_service:
                for day in range(1, int(month_range[1]) + 1):
                    date = str(year_sel) + "-" + str(month_sel).zfill(2) + "-" + str(day).zfill(2)
                    date_db = datetime.date.fromisoformat(date)
                    month_year = str(year_sel) + " " + str(month_sel)
                    is_working_day = request.POST['workd' + str(person.id) + "d" + str(day)]
                    person_id = request.POST['m' + str(person.id) + "d" + str(day)]
                    try:
                        is_sel = request.POST["morning" + str(person.id) + "d" + str(day)]

                        if is_sel == "on":

                            is_extra = "no"

                            try:
                                ex = request.POST["morning_extra" + str(person.id) + "d" + str(day)]
                                if ex == "on":
                                    is_extra = guard_selected.duration_hs
                            except MultiValueDictKeyError:
                                ex = False

                            if int(person_id) == person.id:
                                guard = GuardSheet(
                                    date=date_db,
                                    month_year=month_year,
                                    is_working_day=is_working_day,
                                    shift="Turno mañana",
                                    is_extra=is_extra,
                                    is_active=guard_selected.type,
                                    guard_id=guard_selected,
                                    personal_id=person,
                                )

                                guard.save()

                    except MultiValueDictKeyError:
                        is_selected = False
                    is_working_day = request.POST['workdt' + str(person.id) + "d" + str(day)]
                    person_id = request.POST['t' + str(person.id) + "d" + str(day)]
                    try:
                        is_selt = request.POST["afternoon" + str(person.id) + "d" + str(day)]
                        if is_selt == "on":
                            is_extra = "no"
                            try:
                                ex = request.POST["afternoon_extra" + str(person.id) + "d" + str(day)]
                                if ex == "on":
                                    is_extra = guard_selected.duration_hs
                            except MultiValueDictKeyError:
                                ex = False

                            if int(person_id) == person.id:
                                guard = GuardSheet(
                                    date=date_db,
                                    month_year=month_year,
                                    is_working_day=is_working_day,
                                    is_active=guard_selected.type,
                                    is_extra=is_extra,
                                    shift="Turno tarde",
                                    guard_id=guard_selected,
                                    personal_id=person,
                                )

                                guard.save()

                    except MultiValueDictKeyError:
                        is_selected = False
                    is_working_day = request.POST['workdn' + str(person.id) + "d" + str(day)]
                    person_id = request.POST['n' + str(person.id) + "d" + str(day)]
                    try:
                        is_seln = request.POST["night" + str(person.id) + "d" + str(day)]
                        if is_seln == "on":
                            is_extra = "no"
                            try:
                                ex = request.POST["night_extra" + str(person.id) + "d" + str(day)]
                                if ex == "on":
                                    is_extra = guard_selected.duration_hs
                            except MultiValueDictKeyError:
                                ex = False

                            if int(person_id) == person.id:
                                guard = GuardSheet(
                                    date=date_db,
                                    month_year=month_year,
                                    is_working_day=is_working_day,
                                    is_extra=is_extra,
                                    shift="Turno noche",
                                    is_active=guard_selected.type,
                                    guard_id=guard_selected,
                                    personal_id=person,
                                )

                                guard.save()

                    except MultiValueDictKeyError:
                        is_selected = False
                month_n = month_name[int(month_sel)]

            messages.error(request,
                           f"La planilla del correspondiente a {month_n} de {year_sel} a sido almacenada correctamente")
            return render(request, "planning.html", {'departments': departments,
                                                     'current_month_guard': current_month_guards,
                                                     'previous_month_guards': previous_month_guards,
                                                     'pmn': previous_month_name,
                                                     'month_list': months_list})

    return render(request, "planning.html", {'departments': departments, 'current_month_guard': current_month_guards,
                                             'previous_month_guards': previous_month_guards, 'pmn': previous_month_name,
                                             'month_list': months_list})

# -------------------------------------GET PERSONAL BY SERVICE OR DEPARTMENT-------------------------------


def get_personal_department(request):
    selected_department = request.GET.get('selDepartment')
    department_personal = list(Personal.objects.filter(service_id__department_id=selected_department,
                                                       is_active="yes").values())
    return JsonResponse({"department_personal": department_personal})


def get_personal_service(request):
    selected_department = request.GET.get('selService')
    print(selected_department)
    service_personal = list(Personal.objects.filter(service_id=int(selected_department), is_active="yes").values())
    return JsonResponse({"service_personal": service_personal})


def update_guard(request):
    if request.method == 'POST':
        if request.is_ajax():
            idg = request.POST['id']
            personal_id = request.POST['personal_id']
            is_active = request.POST['is_active']
            guard_day = GuardSheet.objects.get(id=idg)
            guard_day.is_active = is_active

            if personal_id:
                dr = Personal.objects.get(id=int(personal_id))
                guard_day.personal_id = dr

            guard_day.save()
            result = guard_day.personal_id.last_name + ", " + guard_day.personal_id.name
            return HttpResponse(result)

