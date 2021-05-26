from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin


# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=50)
    date_posted = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Departamento Hospital"
        verbose_name_plural = "Departamentos Hospital"

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=50)
    department_id = models.ForeignKey(Department, on_delete=models.PROTECT)
    date_posted = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Servicio Hospital"
        verbose_name_plural = "Servicios Hospital"

    def __str__(self):
        return self.name


class Guard(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    duration_hs = models.CharField(max_length=11)
    service_id = models.ForeignKey(Service, on_delete=models.PROTECT)
    date_posted = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Guardia"
        verbose_name_plural = "Guardias"

    def __str__(self):
        return self.name


class Personal(models.Model):
    file = models.CharField(max_length=30)
    d = models.CharField(max_length=10)
    name = models.CharField(max_length=50, default=" ")
    last_name = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    phone = models.CharField(max_length=11, unique=True)
    is_pro = models.CharField(max_length=10)
    is_active = models.CharField(max_length=10, default='yes')
    service_id = models.ForeignKey(Service, on_delete=models.PROTECT)
    date_posted = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Personal"
        verbose_name_plural = "Personal"

    def __str__(self):
        return self.last_name + ", " + self.name + " - " + self.service_id.name


class GuardSheet(models.Model):
    date = models.DateField()
    month_year = models.CharField(max_length=50)
    is_working_day = models.CharField(max_length=25)
    is_active = models.CharField(max_length=10, default="no")
    shift = models.CharField(max_length=20, default="24")
    personal_amount = models.CharField(max_length=10, default="1")
    guard_id = models.ForeignKey(Guard, on_delete=models.PROTECT)
    personal_id = models.ForeignKey(Personal, on_delete=models.PROTECT)
    is_finish = models.CharField(max_length=10, default="no")
    is_extra = models.CharField(max_length=10, default="no")
    date_posted = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Planilla guardia"
        verbose_name_plural = "Planillas guardias"

    def __str__(self):
        return self.date


class MonthPoints(models.Model):
    month_year = models.CharField(max_length=10)
    passive_working_days = models.CharField(max_length=10)
    passive_working_days_points = models.CharField(max_length=10)
    passive_not_working_days = models.CharField(max_length=10)
    passive_not_working_days_points = models.CharField(max_length=10)
    passive_total_points = models.CharField(max_length=20)
    active_working_days = models.CharField(max_length=10)
    active_working_days_points = models.CharField(max_length=10)
    active_not_working_days = models.CharField(max_length=10)
    active_not_working_days_points = models.CharField(max_length=10)
    active_total_points = models.CharField(max_length=20)
    personal_id = models.ForeignKey(Personal, on_delete=models.PROTECT)
    date_posted = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Planilla puntaje"
        verbose_name_plural = "Planillas puntajes"

    def __str__(self):
        return self.month_year


class MonthHours(models.Model):
    month_year = models.CharField(max_length=10)
    passive_working_days = models.CharField(max_length=10)
    passive_working_days_hours = models.CharField(max_length=10)
    passive_not_working_days = models.CharField(max_length=10)
    passive_not_working_days_hours = models.CharField(max_length=10)
    passive_total_hours = models.CharField(max_length=20)
    active_working_days = models.CharField(max_length=10)
    active_working_days_hours = models.CharField(max_length=10)
    active_not_working_days = models.CharField(max_length=10)
    active_not_working_days_hours = models.CharField(max_length=10)
    active_total_hours = models.CharField(max_length=20)
    personal_id = models.ForeignKey(Personal, on_delete=models.PROTECT)
    date_posted = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Planilla hora extra"
        verbose_name_plural = "Planillas horas extras"

    def __str__(self):
        return self.month_year


class Licences(models.Model):
    name = models.CharField(max_length=50)
    date_posted = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Licencia"
        verbose_name_plural = "Licencias"

    def __str__(self):
        return self.name


class Points(models.Model):
    type = models.CharField(max_length=20)
    day = models.CharField(max_length=20)
    points = models.CharField(max_length=20)
    date_posted = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Punto"
        verbose_name_plural = "Puntos"

    def __str__(self):
        return self.name


class NotWorkingDays(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=50)
    date_posted = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class LicencesDates(models.Model):
    from_date = models.DateField()
    till_date = models.DateField()
    license_id = models.ForeignKey(Licences, on_delete=models.PROTECT)
    personal_id = models.ForeignKey(Personal, on_delete=models.PROTECT)

# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------


class MyAccountManager(BaseUserManager):
    def create_user(self, username, password=None):

        if not username:
            raise ValueError('Debe introducir su número de teléfono')

        if Personal.objects.get(username=username):
            idp = Personal.objects.get(username=username)

            user = self.model(
                username=username,
                personal_id=idp
            )

            user.set_password(password)
            user.save(using=self._db)
            return user
        else:
            raise ValueError('El teléfono introducido no es correcto '
                             'o no existe en la base de datos. Si el numero que ingreso es '
                             'correcto póngase en contacto con el administrador')

    def create_superuser(self, username, password):

        user = self.create_user(
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    class Meta:
        verbose_phone = "Teléfono"


class Account(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=60, unique=True)
    personal_id = models.ForeignKey(Personal, on_delete=models.DO_NOTHING)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'


    objects = MyAccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True





