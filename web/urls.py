"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from login import views as login_views
from home import views as home_views
from inputdata import views as inputdata_views
from planning import views as planning_views
from userview import views as user_views
from reports import views as reports_views
from personal import views as personal_views
from extrahour import views as extrahour_views

urlpatterns = [
    path('', home_views.home, name='home'),
    path('admin/', admin.site.urls),
    path('register/', login_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login/logout.html'), name='logout'),
    path('inputs/', inputdata_views.input_data, name='inputs'),
    path('json-dep', inputdata_views.get_departments, name='json-dep'),
    path('create-dep', inputdata_views.create_department, name='create-dep'),
    path('json-dep-edit', inputdata_views.get_department_edit, name='json-dep-edit'),
    path('update-dep', inputdata_views.update_department, name='update-dep'),
    path('delete-dep', inputdata_views.delete_department, name='delete-dep'),
    path('json-ser', inputdata_views.get_service, name='json-ser'),
    path('create-ser', inputdata_views.create_service, name='create-ser'),
    path('json-ser-edit', inputdata_views.get_service_edit, name='json-ser-edit'),
    path('update-ser', inputdata_views.update_service, name='update-ser'),
    path('delete-ser', inputdata_views.delete_service, name='delete-ser'),
    path('json-guar', inputdata_views.get_guard, name='json-guar'),
    path('create-guar', inputdata_views.create_guard, name='create-guar'),
    path('json-guar-edit', inputdata_views.get_guard_edit, name='json-guar-edit'),
    path('update-guar', inputdata_views.update_guard, name='update-guar'),
    path('delete-guar', inputdata_views.delete_guard, name='delete-guar'),
    path('json-per', inputdata_views.get_personal, name='json-per'),
    path('create-per', inputdata_views.create_personal, name='create-per'),
    path('json-per-edit', inputdata_views.get_personal_edit, name='json-per-edit'),
    path('update-per', inputdata_views.update_personal, name='update-per'),
    path('delete-per', inputdata_views.delete_personal, name='delete-per'),
    path('json-work', inputdata_views.get_notworking, name='json-work'),
    path('create-nowork', inputdata_views.create_notworking, name='create-notw'),
    path('json-notw-edit', inputdata_views.get_notworking_edit, name='json-notw-edit'),
    path('update-nowork', inputdata_views.update_notworking, name='update-nowork'),
    path('delete-nowork', inputdata_views.delete_notworking, name='delete-nowork'),
    path('json-points', inputdata_views.get_points, name='json-points'),
    path('create-points', inputdata_views.create_points, name='create-points'),
    path('json-points-edit', inputdata_views.get_points_edit, name='json-points-edit'),
    path('update-points', inputdata_views.update_points, name='update-points'),
    path('delete-points', inputdata_views.delete_points, name='delete-points'),
    path('json-licences', inputdata_views.get_licences, name='json-licences'),
    path('create-licences', inputdata_views.create_licences, name='create-licences'),
    path('json-licences-edit', inputdata_views.get_licences_edit, name='json-licences-edit'),
    path('update-licences', inputdata_views.update_licences, name='update-licences'),
    path('delete-licences', inputdata_views.delete_licences, name='delete-licences'),
    path('planning/', planning_views.sheets_data, name='planning'),
    path('service/', planning_views.get_personal_service, name='personal-service'),
    path('department/', planning_views.get_personal_department, name='personal-department'),
    path("login_user/", login_views.login_user, name="login_users"),
    path('user/', user_views.inicio_user, name="user-page"),
    path('reports/', reports_views.reports, name='reports'),
    path('update-guard', planning_views.update_guard, name='update-guard'),
    path('personal', personal_views.personal, name='personal'),
    path('list-personal', personal_views.update_personal, name='list-personal'),
    path('personal-data', personal_views.data_personal, name='personal-data'),
    path('get-licences', personal_views.get_licences, name='get-licences'),
    path('save-licenses', personal_views.save_licenses, name='save-licenses'),
    path('delete-license-date', personal_views.delete_licences, name='delete-license-date'),
    path('get-guards', home_views.get_guards, name='get-guards'),
    path('get-guard', home_views.get_guard, name='get-guard'),
    path('create-guard-entry', home_views.create_guard_entry, name='create-guard-entry'),
    path('update-guard-entry', home_views.update_guard_entry, name='update-guard-entry'),
    path('del-guard', home_views.delete_guard, name='del-guard'),
    path('extra', extrahour_views.extra_hours, name='extra')


]
