from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from calendar import monthrange, month_name
import dateutil.relativedelta
import datetime
from inputdata.models import *
from home.decorator import *


@login_required(login_url="login")
@allowed_user(allowed_roles=['admin'])
def extra_hours(request):
    this_month = datetime.datetime.now()
    last_month = this_month + dateutil.relativedelta.relativedelta(months=-1)
    this_month_db = str(this_month.year) + " " + str(this_month.month)
    last_month_db = str(last_month.year) + " " + str(last_month.month)
    mrange = monthrange(int(this_month.year), int(this_month.month))
    month_range = mrange
    month_n = month_name[int(this_month.month)]
    not_workind_days = NotWorkingDays.objects.filter(date__year=this_month.year)
    l_days = []

    if request.method == "POST":
        if "actualizar" in request.POST:
            m = '2021-1'
            dep = request.POST['department']
            ser = request.POST['service']
            guard = request.POST['selected_guard_menu']
            guard_sel = guard
            num_personal = request.POST['num_personal']
            num_personal = int(num_personal)
            number_personal = 1
            personal = Personal.objects.filter(service_id=1, is_active="yes")
            all_personal = Personal.objects.filter(service_id__department_id=1, is_active="yes")
            guard_s = Guard.objects.get(id=1)
            year, mo = m.split("-")
            not_workind_days = NotWorkingDays.objects.filter(date__year=year)
            day_name = ['LUN', 'MAR', 'MIÉ', 'JUE', 'VIE', 'SÁB', 'DOM']

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

                if not GuardSheet.objects.filter(month_year=month_year, guard_id=1):

                    for day in range(1, mrange[1] + 1):
                        x = datetime.date(int(year), int(month), day).isoweekday()
                        date = str(year_sel) + "-" + str(month_sel).zfill(2) + "-" + str(day).zfill(2)
                        date_db = datetime.date.fromisoformat(date)

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
                            l_days.append(y)

                    list_days = l_days


                    return render(request, "extra.html",
                                  {"l_days": l_days, "month": month_n, "year": year, 'guardm': guard_s,
                                   'personal': personal, 'range': range(num_personal),
                                   'num_personal':num_personal, 'pasive':pasive})

                else:
                    messages.error(request,
                                   f"La planilla {guard_s} correspondiente a {month_n} de {year_s} "
                                   f"ya existe, para editarla o visualizarla seleccionela de la lista")


    return render(request, "extra.html")

