# Generated by Django 3.1.6 on 2021-04-02 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date_posted', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Departamento Hospital',
                'verbose_name_plural': 'Departamentos Hospital',
            },
        ),
        migrations.CreateModel(
            name='Guard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('duration_hs', models.CharField(max_length=11)),
                ('date_posted', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Guardia',
                'verbose_name_plural': 'Guardias',
            },
        ),
        migrations.CreateModel(
            name='Licences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date_posted', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Licencia',
                'verbose_name_plural': 'Licencias',
            },
        ),
        migrations.CreateModel(
            name='NotWorkingDays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=50)),
                ('date_posted', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Points',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
                ('day', models.CharField(max_length=20)),
                ('points', models.CharField(max_length=20)),
                ('date_posted', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Punto',
                'verbose_name_plural': 'Puntos',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date_posted', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inputdata.department')),
            ],
            options={
                'verbose_name': 'Servicio Hospital',
                'verbose_name_plural': 'Servicios Hospital',
            },
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.CharField(max_length=30)),
                ('d', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('profession', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=11)),
                ('is_pro', models.CharField(max_length=10)),
                ('is_active', models.CharField(default='yes', max_length=10)),
                ('date_posted', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('service_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inputdata.service')),
            ],
            options={
                'verbose_name': 'Personal',
                'verbose_name_plural': 'Personal',
            },
        ),
        migrations.CreateModel(
            name='MonthPoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_year', models.CharField(max_length=10)),
                ('passive_working_days', models.CharField(max_length=10)),
                ('passive_working_days_points', models.CharField(max_length=10)),
                ('passive_not_working_days', models.CharField(max_length=10)),
                ('passive_not_working_days_points', models.CharField(max_length=10)),
                ('passive_total_points', models.CharField(max_length=20)),
                ('active_working_days', models.CharField(max_length=10)),
                ('active_working_days_points', models.CharField(max_length=10)),
                ('active_not_working_days', models.CharField(max_length=10)),
                ('active_not_working_days_points', models.CharField(max_length=10)),
                ('active_total_points', models.CharField(max_length=20)),
                ('license', models.CharField(default='no', max_length=50)),
                ('date_posted', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('guard_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inputdata.guard')),
                ('personal_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inputdata.personal')),
            ],
            options={
                'verbose_name': 'Planilla puntaje',
                'verbose_name_plural': 'Planillas puntajes',
            },
        ),
        migrations.CreateModel(
            name='LicencesDates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField()),
                ('till_date', models.DateField()),
                ('license_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inputdata.licences')),
                ('personal_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inputdata.personal')),
            ],
        ),
        migrations.CreateModel(
            name='GuardSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('month_year', models.CharField(max_length=50)),
                ('is_working_day', models.CharField(max_length=25)),
                ('is_active', models.CharField(default='no', max_length=10)),
                ('shift', models.CharField(default='24', max_length=20)),
                ('personal_amount', models.CharField(default='1', max_length=10)),
                ('is_finish', models.CharField(default='no', max_length=10)),
                ('is_extra', models.CharField(default='no', max_length=10)),
                ('date_posted', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('guard_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inputdata.guard')),
                ('personal_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inputdata.personal')),
            ],
            options={
                'verbose_name': 'Planilla guardia',
                'verbose_name_plural': 'Planillas guardias',
            },
        ),
        migrations.AddField(
            model_name='guard',
            name='service_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inputdata.service'),
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('username', models.CharField(max_length=60, unique=True)),
                ('phone', models.CharField(max_length=11, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('personal_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='inputdata.personal')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
    ]