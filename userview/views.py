from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from inputdata.models import *
import datetime
from datetime import timedelta

# Create your views here.


@login_required(login_url="login_users")
def inicio_user(request):
    department_list = Department.objects.all()
    current_date = datetime.datetime.now()
    fecha = str(current_date.year) + "-" + str(current_date.month).zfill(2) + "-" + str(current_date.day).zfill(2)
    fechadb = datetime.date.fromisoformat(fecha)
    fechadbnext = fechadb + timedelta(days=1)
    fechadbprev = fechadb - timedelta(days=1)
    fecha_plus = fechadb + timedelta(days=30)
    time = current_date.hour
    month_year = str(current_date.year) + " " + str(current_date.month)

    current_guard = GuardSheet.objects.filter(date=fechadb)
    current_guard_next = GuardSheet.objects.filter(date=fechadbnext)
    guar= Guard.objects.get(name="Guardia de medicina general")
    guar_obito = Guard.objects.get(name="Constatación óbito")
    guard_id = guar.id
    obito_id = guar_obito
    now_obito = GuardSheet.objects.get(date=fechadb, guard_id=obito_id)
    next_obito = GuardSheet.objects.get(date=fechadbnext, guard_id=obito_id)
    prev_obito = GuardSheet.objects.get(date=fechadbprev, guard_id=obito_id)
    guard_prev = GuardSheet.objects.get(date=fechadbprev, guard_id=guard_id)
    guard_now = GuardSheet.objects.get(date=fechadb, guard_id=guard_id)
    guard_next = GuardSheet.objects.get(date=fechadbnext, guard_id=guard_id)

    user_id = request.user.personal_id
    next_user_guard = "0"
    user_guards = GuardSheet.objects.filter(personal_id=user_id, date__range=[fechadb, fecha_plus]).order_by('date')
    if len(user_guards) > 0:
        next_user_guard = str(user_guards[0].date.strftime("%A"))+" "+str(user_guards[0].date.strftime("%d")) + ", " \
                          + str(user_guards[0].guard_id.name)
    guards_user_service = []
    guards = Guard.objects.filter(service_id=request.user.personal_id.service_id.id)
    user_total = []

    for g in guards:
        if GuardSheet.objects.filter(guard_id=g.id, month_year=month_year).order_by('date'):
            x = GuardSheet.objects.filter(guard_id=g.id, month_year=month_year).order_by('date')
            guards_user_service.append(x)
            guard = []
            total = int()
            nwd = int()
            wd = int()
            guard.append(g.name)
            for y in x:
                if y.personal_id == user_id:
                    total += 1
                    if y.is_working_day != "Hábil":
                        nwd += 1
                    else:
                        wd += 1
            guard.append(total)
            guard.append(wd)
            guard.append(nwd)
            user_total.append(guard)

    return render(request, "home_user.html",
                  {"department": department_list, 'current': current_guard, 'next': current_guard_next,
                   'prev': guard_prev, 'time': time, 'prev_obito': prev_obito, 'now_obito': now_obito, 'now': guard_now,
                   'next_obito': next_obito, 'guard_next': guard_next, 'tomorrow': fechadbnext,
                   'user_guards': next_user_guard, 'calendar': guards_user_service, 'total': user_total})