from rest_framework import serializers
from inputdata.models import *


class GuardsheetsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='personal_id.name')
    last_name = serializers.CharField(source='personal_id.last_name')
    guard = serializers.CharField(source='guard_id.name')
    duration = serializers.CharField(source='guard_id.duration_hs')
    date_name = serializers.CharField(source='date')
    class Meta:
        model = GuardSheet
        fields = ('id',
                  'date',
                  'month_year',
                  'is_working_day',
                  'is_active',
                  'shift',
                  'personal_amount',
                  'guard_id',
                  'duration',
                  'personal_id',
                  'name',
                  'date_name',
                  'guard',
                  'last_name',
                  'is_finish',
                  'is_extra',)


