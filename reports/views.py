from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from inputdata.models import GuardSheet
from home.decorator import *
from inputdata.models import *
import calendar


@login_required(login_url="login")
@allowed_user(allowed_roles=['admin'])
def reports(request):
    departments = Department.objects.all()

    current_date = datetime.datetime.now()
    month = str(current_date.year) + " " + str(current_date.month)
    m_range = calendar.monthrange(current_date.year, current_date.month)
    first = str(current_date.year) + "-" + str(current_date.month).zfill(2) + "-" + str(1).zfill(2)
    last = str(current_date.year) + "-" + str(current_date.month).zfill(2) + "-" + str(m_range[1]).zfill(2)
    first_day = datetime.date.fromisoformat(first)
    last_day = datetime.date.fromisoformat(last)

    services = Service.objects.all()
    persona = Personal.objects.filter(is_pro="true", is_active="yes")

    info = []
    points = Points.objects.all()
    ah = 0
    anh = 0
    ph = 0
    pnh = 0

    for po in points:
        if po.type == "Activa" and po.day == "Día hábil":
            ah = po.points
        elif po.type == "Activa" and po.day == "Día no hábil":
            anh = po.points
        elif po.type == "Pasiva" and po.day == "Día hábil":
            ph = po.points
        elif po.type == "Pasiva" and po.day == "Día no hábil":
            pnh = po.points

    for per in persona:
        x = []
        x.append(per)

        guards = GuardSheet.objects.filter(month_year=month, personal_id=per)
        puntos_activa_habil = 0
        puntos_activa_nohabil = 0
        puntos_pasiva_habil = 0
        puntos_pasiva_nohabil = 0
        dias_activa_habil = 0
        dias_activa_nohabil = 0
        dias_pasiva_habil = 0
        dias_pasiva_nohabil = 0
        activa_habil = []
        activa_nohabil = []
        pasiva_habil = []
        pasiva_nohabil = []
        for gua in guards:
            if gua.is_working_day == "Hábil" and gua.is_active == "activa":
                dias_activa_habil += 1
                puntos_activa_habil += int(ah)
            elif gua.is_working_day == "Hábil" and gua.is_active == "pasiva":
                dias_pasiva_habil += 1
                puntos_pasiva_habil += int(ph)
            elif gua.is_working_day == "No hábil" and gua.is_active == "activa":
                dias_activa_nohabil += 1
                puntos_activa_nohabil += int(anh)
            elif gua.is_working_day == "No hábil" and gua.is_active == "pasiva":
                dias_pasiva_nohabil += 1
                puntos_pasiva_nohabil += int(pnh)
            elif gua.is_working_day == "Fin de semana" and gua.is_active == "activa":
                dias_activa_nohabil += 1
                puntos_activa_nohabil += int(anh)
            elif gua.is_working_day == "Fin de semana" and gua.is_active == "pasiva":
                dias_pasiva_nohabil += 1
                puntos_pasiva_nohabil += int(pnh)
        activa_habil.append(dias_activa_habil)
        activa_habil.append(puntos_activa_habil)
        x.append(activa_habil)
        activa_nohabil.append(dias_activa_nohabil)
        activa_nohabil.append(puntos_activa_nohabil)
        x.append(activa_nohabil)
        x.append(puntos_activa_nohabil + puntos_activa_habil)
        pasiva_habil.append(dias_pasiva_habil)
        pasiva_habil.append(puntos_pasiva_habil)
        x.append(pasiva_habil)
        pasiva_nohabil.append(dias_pasiva_nohabil)
        pasiva_nohabil.append(puntos_pasiva_nohabil)
        x.append(pasiva_nohabil)
        x.append(puntos_pasiva_nohabil + puntos_pasiva_habil)
        if LicencesDates.objects.filter(personal_id=per, from_date__range=(first_day, last_day)):
            licences = LicencesDates.objects.filter(personal_id=per, from_date__range=[first_day, last_day])
            x.append(licences)
        info.append(x)

    return render(request, "reports.html", {'departments': departments, "info": info})
